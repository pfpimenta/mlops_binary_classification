# -*- coding: utf-8 -*-
# This script contains the endpoints for the WebAPI

from flask import Flask

from classify import classify_batch, classify_sample
from healthcheck import check_health
from train import train

app = Flask(__name__)

# hello world checkpoint (to test if API is up)
@app.route("/")
def hello_world():
    app.logger.info("Processing default request")
    return "Hello World!"


# healthcheck endpoint
@app.route("/healthcheck", methods=["GET"])
def endpoint_healthcheck():
    health = check_health()
    app.logger.info("Current system health: ", str(health))
    return health


# endpoint to train the model
# TODO
@app.route("/train", methods=["GET"])
def endpoint_train():
    app.logger.info("Training the model...")
    # TODO refactor
    model, score = train()  # TODO save model state somehow
    return (
        f"Model has been trained successfully. Score on the test data: {score}\n",
        200,
    )


# endpoint to classify a single sample
# TODO
@app.route("/classify_sample", methods=["GET"])
def endpoint_classify_sample(sample):
    # logging.debug("Classifying sample: %s", str(sample))
    predicted_class = classify_sample(sample)
    # TODO log readable string with the result
    return predicted_class, 200


# endpoint to classify a batch of samples
# TODO
@app.route("/classify_batch", methods=["GET"])
def endpoint_classify_batch(batch: list) -> list:
    num_samples = len(batch)
    # logging.debug("Classifying batch with %s samples", num_samples)
    predicted_batch_classes = classify_batch(batch)
    return predicted_batch_classes


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9200)
