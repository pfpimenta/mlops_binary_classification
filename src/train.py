# -*- coding: utf-8 -*-
# functions for training, saving and loading the model

import glob
import os
from datetime import datetime

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
    date_string = f"{datetime.now():%Y-%m-%d_%H:%M:%S%z}"
    model_name = "model_" + date_string
    model_filepath = MODEL_FOLDERPATH + model_name + ".joblib"
    if not os.path.exists(MODEL_FOLDERPATH):
        os.makedirs(MODEL_FOLDERPATH)
    dump(model, model_filepath)


def find_latest_model_filepath() -> str:
    """
        returns filepath of the most recent model saved
    """
    search_filepath = MODEL_FOLDERPATH + "model_*.joblib"
    filepaths = glob.glob(search_filepath)
    if not filepaths:  # no saved model found
        raise Exception("Model not found")
    model_filepath = sorted(filepaths)[-1]  # get most recent model
    return model_filepath


def load_model(model_name=None):
    """
        loads and returns the model with model_name
        if model_name is not given, returns the most recent model saved
    """
    if model_name is None:
        model_filepath = find_latest_model_filepath()
    else:
        model_filepath = MODEL_FOLDERPATH + model_name + ".joblib"
    model = load(model_filepath)
    return model
