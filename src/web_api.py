# This script contains the endpoints for the WebAPI

from flask import Flask

app = Flask(__name__)

# healthcheck endpoint
# TODO

# endpoint to train the model
# TODO

# endpoint to classify a single sample
# TODO
@app.route('/classify_sample', methods=['GET'])
def endpoint_classify_sample():
    pass

# endpoint to classify a batch of samples
# TODO
