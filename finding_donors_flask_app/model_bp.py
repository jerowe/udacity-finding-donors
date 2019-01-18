from sklearn.metrics import fbeta_score, accuracy_score
import pandas as pd
import numpy as np
from time import time
from flask import Blueprint, jsonify, request
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
import json
import redis
from pprint import pprint
from data_bp import data
from sklearn.model_selection import train_test_split

redis_client = redis.Redis(host='redis', port=6379, db=0)

# try:
#     from .data_bp import data
# except:

model_bp = Blueprint('finding-donors-model', __name__)
models = {
    'SVC': SVC(gamma='auto', random_state=1),
    'KNeighborsClassifier': KNeighborsClassifier(),
    'GaussianNB': GaussianNB(),
    'ADABoostClassifier': AdaBoostClassifier(random_state=1),
    'RandomForestClassifier': RandomForestClassifier(random_state=1),
    'GradientBoostingClassifier': GradientBoostingClassifier(random_state=1)
}


@model_bp.route('/train', methods=['POST'])
def train():
    """

    :param model_name:
    :param sample_size:
    :return:
    """
    X_train, X_test, y_train, y_test = return_train_test_data()
    request_data = json.loads(request.data.decode('utf-8'))
    pprint('Request data')
    pprint(request_data)
    if not 'model_name' in request_data:
        raise Exception('You must define a model name!')
    else:
        model_name = request_data.get('model_name')

    total_records = round(len(y_train))
    if not 'sample_size' in request_data:
        sample_size = round(len(y_train))
    else:
        sample_size = int(request_data.get('sample_size'))
        if sample_size > total_records:
            sample_size = total_records

    model = get_model(model_name)
    results = train_predict(model, sample_size, X_train, y_train, X_test, y_test)
    return jsonify(results)


def train_in_background():
    X_train, X_test, y_train, y_test = return_train_test_data()
    sample_size = round(len(y_train))
    for model_name in models:
        for sample_size in [100, 1000, 10000, 20000, 30000, sample_size]:
            model = get_model(model_name)
            train_predict(model, sample_size, X_train, y_train, X_test, y_test)


def get_model(model_name='ADABoostClassifier'):
    if not model_name in models:
        raise Exception('{} not in list of allowed models'.format(model_name))
    else:
        return models[model_name]


def train_predict(learner, sample_size, X_train, y_train, X_test, y_test):
    """
     inputs:
        - learner: the learning algorithm to be trained and predicted on
        - sample_size: the size of samples (number) to be drawn from training set
        - X_train: features training set
        - y_train: income training set
        - X_test: features testing set
        - y_test: income testing set
    """

    learner_name = learner.__class__.__name__

    redis_key = '{}-{}'.format(learner_name, sample_size)
    if redis_client.get(redis_key):
        results = json.loads(redis_client.get(redis_key).decode('utf-8'))
        results['fetched_from_cache'] = True
        return results
    else:
        results = {}
        results['model'] = learner_name
        results['sample_size'] = sample_size
        results['fetched_from_cache'] = False

        start = time()  # Get start time
        # Train!
        pprint('Training data size')
        pprint(X_train[:sample_size].shape)

        learner = learner.fit(X_train[:sample_size], y_train[:sample_size])
        end = time()  # Get end time

        results['train_time'] = end - start

        start = time()  # Get start time
        # Predict!
        predictions_test = learner.predict(X_test)
        predictions_train = learner.predict(X_train[:sample_size])
        end = time()  # Get end time

        results['pred_time'] = end - start

        results['acc_train'] = accuracy_score(y_train[:sample_size], predictions_train)

        results['acc_test'] = accuracy_score(y_test, predictions_test)

        results['f_train'] = fbeta_score(y_train[:sample_size], pd.Series(predictions_train, dtype=int), beta=0.5,
                                         average='weighted', labels=np.unique(predictions_test))

        results['f_test'] = fbeta_score(y_test, pd.Series(predictions_test, dtype=int), beta=0.5, average='weighted',
                                        labels=np.unique(predictions_test))

        # Return the results
        redis_client.set(redis_key, json.dumps(results))
        return results


def return_train_test_data():
    features_final, income = preprocess_data()
    return train_test_split(features_final,
                            income,
                            test_size=0.2,
                            random_state=1)


def preprocess_data():
    # Log-transform the skewed features
    income_raw = data['income']
    features_raw = data.drop('income', axis=1)
    skewed = ['capital-gain', 'capital-loss']
    features_log_transformed = pd.DataFrame(data=features_raw)
    features_log_transformed[skewed] = features_raw[skewed].apply(lambda x: np.log(x + 1))
    scaler = MinMaxScaler()  # default=(0, 1)
    numerical = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']

    features_log_minmax_transform = pd.DataFrame(data=features_log_transformed)
    features_log_minmax_transform[numerical] = scaler.fit_transform(features_log_transformed[numerical])

    features_final_t = pd.get_dummies(features_log_minmax_transform)
    replace = {'<=50K': 0, '>50K': 1}
    income_t = income_raw.replace(replace, inplace=False)

    # Print the number of features after one-hot encoding
    # encoded = list(features_final.columns)
    return features_final_t, income_t


# Since we're sticking all this in a redis cache anyways
# Just train when the web server comes up

train_in_background()

