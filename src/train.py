# -*- coding: utf-8 -*-
# functions for training, saving and loading the model

import os

from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier

from const import MODEL_FOLDERPATH
from data_loader import get_training_data
from model_validation import validate_model


def train_model():
    train_X, train_Y = get_training_data()
    model = RandomForestClassifier(random_state=0)
    model.fit(train_X, train_Y)
    return model


# function called by the /train endpoint
def train():
    model = train_model()
    is_model_valid, score = validate_model(model)
    if is_model_valid is False:
        raise Exception("Invalid model.")
    else:
        save_model(model)
        return score


def save_model(model):
    model_name = "seila"  # TODO change this
    model_filepath = MODEL_FOLDERPATH + model_name + ".joblib"
    if not os.path.exists(MODEL_FOLDERPATH):
        os.makedirs(MODEL_FOLDERPATH)
    dump(model, model_filepath)


def load_model(model_name=None):
    if model_name is None:
        model_name = "seila"  # TODO change this
    model_filepath = MODEL_FOLDERPATH + model_name + ".joblib"
    model = load(model_filepath)
    return model
