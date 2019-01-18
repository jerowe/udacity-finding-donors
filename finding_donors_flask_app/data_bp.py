import numpy as np
import pandas as pd
from time import time
import os
import functools
from collections import Counter
from flask import Blueprint, jsonify, request
import json
import redis
from sklearn.preprocessing import MinMaxScaler

redis_client = redis.Redis(host='redis', port=6379, db=0)

# ON AWS This fails and tells me to try engine=python
data = pd.read_csv(os.environ.get('DONOR_DATA'), engine='python')

numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
data_less_than_50k = data[data['income'] == '<=50K']
data_greater_than_50k = data[data['income'] == '>50K']
object_columns = ['workclass', 'education_level', 'marital-status', 'occupation', 'relationship', 'race', 'sex',
                  'native-country']
numeric_columns = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']

data_bp = Blueprint('finding-donors-data', __name__)


@data_bp.route('/get-frequencies', methods=['GET'])
def frequencies():
    results = {}
    if redis_client.get('get-frequencies'):
        return redis_client.get('get-frequencies').decode('utf-8')
    else:
        for col_name in list(data):
            results[col_name] = frequency(col_name)
        return jsonify(results)


@data_bp.route('/read-data', methods=['GET'])
def read_data():
    return data.to_json(orient='records')


@data_bp.route('/get-stats', methods=['GET'])
def get_stats():
    if redis_client.get('get-stats'):
        return redis_client.get('get-stats').decode('utf-8')
    else:
        results = {}
        for col in numeric_columns:
            results[col] = get_col_stats(data[col])
        return jsonify(results)


@data_bp.route('/get-correlation', methods=['GET'])
def get_correlation():
    replace = {'<=50K': 0, '>50K': 1}
    encoded_income = data.replace(replace, inplace=False)
    return encoded_income.corr().to_json()


@data_bp.route('/get-correlation-feature-transformation', methods=['GET'])
def get_correlation_feature_transformation():
    replace = {'<=50K': 0, '>50K': 1}
    encoded_income = data.replace(replace, inplace=False)
    skewed = ['capital-gain', 'capital-loss']
    features_log_transformed = pd.DataFrame(data=encoded_income)
    features_log_transformed[skewed] = data[skewed].apply(lambda x: np.log(x + 1))
    # Initialize a scaler, then apply it to the features
    scaler = MinMaxScaler()  # default=(0, 1)
    numerical = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']

    features_log_minmax_transform = pd.DataFrame(data=features_log_transformed)
    features_log_minmax_transform[numerical] = scaler.fit_transform(features_log_transformed[numerical])


def get_col_stats(values):
    """This route can't be hashes, 'Series objects are mutable'"""
    results = {}
    minimum = values.min()
    maximum = values.max()
    mean = values.mean()
    median = values.median()
    std = values.std()
    results['std'] = "{0:.2f}".format(float(std))
    results['minimum'] = "{0:.2f}".format(float(minimum))
    results['maximum'] = "{0:.2f}".format(float(maximum))
    results['mean'] = "{0:.2f}".format(float(mean))
    results['median'] = "{0:.2f}".format(float(median))
    return results


@functools.lru_cache(maxsize=100)
def frequency(col_name='income'):
    """
    TODO If this is numeric it should probably be binned
    :param col_name: column name from the data frame
    :type str
    :return: dict of frequency of values
    """

    return Counter(list(data[col_name]))


@data_bp.route('/get-frequencies-by-income', methods=['GET'])
def get_frequency_by_income():
    """
    Return frequency of data as a function of income
    :return:
    """
    if redis_client.get('get-frequencies-by-income'):
        return redis_client.get('get-frequencies-by-income').decode('utf-8')
    else:
        results = {}
        for col in object_columns:
            g = Counter(list(data_greater_than_50k[col]))
            l = Counter(list(data_less_than_50k[col]))
            results[col] = {'g': g, 'l': l}

        return jsonify(results)
