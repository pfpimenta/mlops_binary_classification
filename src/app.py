# -*- coding: utf-8 -*-
# This script contains the endpoints for the WebAPI

import os
from json import loads

import pandas as pd
from flask import Flask, jsonify, request

from classify import classify_batch, classify_sample, classify_test_sample
from flask_logs import LogSetup
from healthcheck import check_health
from train import train

# setup app
app = Flask(__name__)
# setup logging configs
app.config["LOG_TYPE"] = os.environ.get("LOG_TYPE", "stream")
app.config["LOG_LEVEL"] = os.environ.get("LOG_LEVEL", "DEBUG")
logs = LogSetup()
logs.init_app(app)

# hello world checkpoint (to test if API is up)
@app.route("/")
def hello_world():
    app.logger.info("Processing default request")
    return "Hello World!\n"


# healthcheck endpoint
@app.route("/healthcheck", methods=["GET"])
def endpoint_healthcheck():
    is_ok, details = check_health()
    app.logger.info("Current system health: %s", details)
    return jsonify(ok=is_ok, _details=details)


# endpoint to train the model
# TODO
@app.route("/train", methods=["GET"])
def endpoint_train():
    app.logger.info("Training the model...")
    score = train()
    message = f"Model has been trained successfully. Score on the test data: {score}"
    app.logger.info(message)
    return jsonify(message=message, score=(score)), 200


# endpoint to classify a test sample (for debug purposes)
@app.route("/classify_test_sample", methods=["GET"])
def endpoint_classify_test_sample():
    predicted_class, expected_class = classify_test_sample()
    app.logger.info("Predicted class: %s", str(predicted_class))
    app.logger.info("Expected class: %s", str(expected_class))
    return (
        jsonify(predicted_class=predicted_class, expected_class=expected_class),
        200,
    )


# endpoint to classify a single sample
@app.route("/classify_sample/", methods=["GET"])
def endpoint_classify_sample():
    sample_json = request.args.get("sample")
    app.logger.info("Classifying sample: %s", sample_json)
    sample = pd.DataFrame(loads(sample_json))
    predicted_class = classify_sample(sample)
    app.logger.info("Result: %s", str(predicted_class))
    return jsonify(predicted_class=str(predicted_class)), 200


# endpoint to classify a batch of samples
@app.route("/classify_batch", methods=["GET"])
def endpoint_classify_batch():
    batch_json = request.args.get("batch")
    batch = [pd.DataFrame(sample) for sample in loads(batch_json)]
    num_samples = len(batch)
    app.logger.info("Classifying batch with %s samples", num_samples)
    predicted_batch_classes = classify_batch(batch)
    app.logger.info("Result: %s", str(predicted_batch_classes))
    return jsonify(predicted_batch_classes=str(predicted_batch_classes)), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9200)
