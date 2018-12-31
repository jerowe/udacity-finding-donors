from sklearn.metrics import fbeta_score, accuracy_score
import pandas as pd
import numpy as np
from time import time
from flask import Blueprint, jsonify, request

model_bp = Blueprint('finding-donors-model', __name__)


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

    results = {}

    start = time()  # Get start time
    learner = learner.fit(X_train[:sample_size], y_train[:sample_size])
    end = time()  # Get end time

    # TODO: Calculate the training time
    results['train_time'] = end - start

    start = time()  # Get start time
    predictions_test = learner.predict(X_test)
    predictions_train = learner.predict(X_train[:sample_size])
    end = time()  # Get end time

    # TODO: Calculate the total prediction time
    results['pred_time'] = end - start

    # TODO: Compute accuracy on the first 300 training samples which is y_train[:300]
    results['acc_train'] = accuracy_score(y_train[:sample_size], predictions_train)

    # TODO: Compute accuracy on test set using accuracy_score()
    results['acc_test'] = accuracy_score(y_test, predictions_test)

    # TODO: Compute F-score on the the first 300 training samples using fbeta_score()
    results['f_train'] = fbeta_score(y_train[:sample_size], pd.Series(predictions_train, dtype=int), beta=0.5,
                                     average='weighted', labels=np.unique(predictions_test))

    # TODO: Compute F-score on the test set which is y_test
    results['f_test'] = fbeta_score(y_test, pd.Series(predictions_test, dtype=int), beta=0.5, average='weighted',
                                    labels=np.unique(predictions_test))

    # Success
    print("{} trained on {} samples.".format(learner.__class__.__name__, sample_size))

    # Return the results
    return results
