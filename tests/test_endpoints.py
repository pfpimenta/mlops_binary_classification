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
    r = requests.get(url=URL + "healthcheck")
    response_data = r.json()
    assert response_data["ok"]


def test_train():
    r = requests.get(url=URL + "train")
    response_data = r.json()
    score = response_data["score"]
    is_float = isinstance(score, float)
    assert is_float


def test_classify_test_sample():
    r = requests.get(url=URL + "classify_test_sample")
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
        sample_data[feature] = [random()]
    return sample_data


def test_classify_sample():
    sample = get_random_sample()
    parameters = {"sample": dumps(sample)}
    r = requests.get(url=URL + "classify_sample", params=parameters)
    response_data = r.json()
    print(response_data)
    # TODO assert


def get_random_batch(batch_size):
    random_batch = [get_random_sample() for i in range(batch_size)]
    return random_batch


def test_classify_batch():
    batch_size = 10
    batch = get_random_batch(batch_size)
    parameters = {"batch": dumps(batch)}
    r = requests.get(url=URL + "classify_batch", params=parameters)
    response_data = r.json()
    print(response_data)
    # TODO assert
