# -*- coding: utf-8 -*-
# This script contains the endpoints for the WebAPI

# pytest==6.2.2
# pandas==1.0.5
# requests

from json import dumps
from random import random

import pandas as pd
import pytest
import requests

SAMPLE_FEATURES = ["Time"] + ["V" + str(i) for i in range(1, 29)] + ["Amount"]

URL = "http://0.0.0.0:9200/"


def test_healthcheck():
    endpoint = "healthcheck"
    r = requests.get(url=URL + endpoint)
    response_data = r.json()
    assert response_data["ok"]


def test_train():
    endpoint = "train"
    r = requests.get(url=URL + endpoint)
    response_data = r.json()
    assert list(response_data.keys()) == ["message", "metrics"]
    metrics = response_data["metrics"]
    is_dict = isinstance(metrics, dict)
    assert is_dict
    for _, value in metrics.items():
        assert isinstance(value, float)
        assert value >= 0 and value <= 1


def test_classify_random_sample():
    endpoint = "classify_random_sample"
    r = requests.get(url=URL + endpoint)
    response_data = r.json()
    assert list(response_data.keys()) == ["expected_class", "predicted_class"]
    expected_class = response_data["expected_class"]
    predicted_class = response_data["predicted_class"]
    assert isinstance(expected_class, int)
    assert isinstance(predicted_class, int)
    assert expected_class in [0, 1]
    assert predicted_class in [0, 1]


def get_random_sample():
    sample_data = {}
    for feature in SAMPLE_FEATURES:
        sample_data[feature] = [random() * 10 - 5]
    return sample_data


def test_classify_sample():
    sample = get_random_sample()
    parameters = {"sample": dumps(sample)}
    endpoint = "classify_sample"
    r = requests.get(url=URL + endpoint, params=parameters)
    response_data = r.json()
    assert list(response_data.keys()) == ["message", "predicted_class"]
    predicted_class = response_data["predicted_class"]
    assert isinstance(predicted_class, int)
    assert predicted_class in [0, 1]


def get_random_batch(batch_size):
    random_batch = [get_random_sample() for i in range(batch_size)]
    return random_batch


def test_classify_batch():
    batch_size = 10
    batch = get_random_batch(batch_size)
    parameters = {"batch": dumps(batch)}
    endpoint = "classify_batch"
    r = requests.get(url=URL + endpoint, params=parameters)
    response_data = r.json()
    assert list(response_data.keys()) == ["message", "predicted_batch_classes"]
    predicted_batch_classes = response_data["predicted_batch_classes"]
    assert isinstance(predicted_batch_classes, list)
    assert len(predicted_batch_classes) == batch_size
    for predicted_sample_class in predicted_batch_classes:
        assert isinstance(predicted_sample_class, int)
        assert predicted_sample_class in [0, 1]
