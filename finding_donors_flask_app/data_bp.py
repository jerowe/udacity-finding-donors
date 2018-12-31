import numpy as np
import pandas as pd
from time import time
import os
import functools
from collections import Counter
from flask import Blueprint, jsonify, request
import json

data = pd.read_csv(os.environ.get('DONOR_DATA'))

data_bp = Blueprint('finding-donors-data', __name__)


@data_bp.route('/get-frequencies', methods=['GET'])
def frequencies():
    results = {}
    for col_name in list(data):
        results[col_name] = frequency(col_name)
    return jsonify(results)


@data_bp.route('/read-data', methods=['GET'])
def read_data():
    return data.to_json(orient='records')


@data_bp.route('/get-stats', methods=['GET'])
def get_stats():
    results = {}
    for col in list(data):
        results[col] = get_col_stats(data[col])
    return jsonify(results)


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

    :param col_name: column name from the data frame
    :type str
    :return: dict of frequency of values
    """
    return Counter(list(data[col_name]))
