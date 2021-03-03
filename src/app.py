# -*- coding: utf-8 -*-
# This script contains the endpoints for the WebAPI

import logging

from flask import Flask

from src.healthcheck import check_health

app = Flask(__name__)

# healthcheck endpoint
# TODO
@app.route("/healthcheck", methods=["GET"])
def endpoint_healthcheck():
    health = check_health()
    logging.info("Current system health: %s", health)
    return


# endpoint to train the model
# TODO

# endpoint to classify a single sample
# TODO
@app.route("/classify_sample", methods=["GET"])
def endpoint_classify_sample(sample):
    logging.debug("Classifying sample: %s")
    pass


# endpoint to classify a batch of samples
# TODO
@app.route("/classify_sample", methods=["GET"])
def endpoint_classify_sample(batch: list) -> list:
    num_samples = len(batch)
    logging.debug("Classifying batch with %s samples", num_samples)
    pass
