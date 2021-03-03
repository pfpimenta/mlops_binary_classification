# -*- coding: utf-8 -*-
# This script contains the endpoints for the WebAPI

import logging

from flask import Flask

from healthcheck import check_health
from train import train_model
from classify import classify_sample, classify_batch

app = Flask(__name__)

# healthcheck endpoint
# TODO
@app.route("/healthcheck", methods=["GET"])
def endpoint_healthcheck():
    health = check_health()
    logging("Current system health: " + str(health))
    return health, 200


# endpoint to train the model
# TODO
@app.route("/classify_sample", methods=["GET"])
def endpoint_train():
    logging.debug("Training the model...")
    train_model()
    return "Model has successfully trained", 200

# endpoint to classify a single sample
# TODO
@app.route("/classify_sample", methods=["GET"])
def endpoint_classify_sample(sample):
    logging.debug("Classifying sample: %s", str(sample))
    # TODO : validate sample data
    return "The given ", 200


# endpoint to classify a batch of samples
# TODO
@app.route("/classify_batch", methods=["GET"])
def endpoint_classify_batch(batch: list) -> list:
    num_samples = len(batch)
    logging.debug("Classifying batch with %s samples", num_samples)
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9200)