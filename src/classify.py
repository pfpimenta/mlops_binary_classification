# -*- coding: utf-8 -*-
# functions that use the trained model to classify a sample or a batch

from data_loader import get_one_sample, get_random_sample
from data_validation import validate_sample
from model_validation import validate_model
from train import load_model


def classify_sample(sample) -> bool:
    """ classifies one sample """
    is_sample_valid = validate_sample(sample)
    if is_sample_valid is False:
        raise Exception("Invalid sample")
    model = load_model()
    is_model_valid, _ = validate_model(model)
    if is_model_valid is False:
        raise Exception("Invalid model")
    predicted_class = int(model.predict(sample)[0])
    return predicted_class


def classify_batch(batch) -> list:
    """ classifies one batch of samples """
    predicted_batch_classes = [classify_sample(sample) for sample in batch]
    return predicted_batch_classes


def classify_one_sample() -> (int, int):
    """ loads one test sample and classifies it """
    sample, sample_class = get_one_sample()
    predicted_class = classify_sample(sample)
    return predicted_class, sample_class


def classify_random_sample() -> (int, int):
    """ loads one random test sample and classifies it """
    sample, sample_class = get_random_sample()
    predicted_class = classify_sample(sample)
    return predicted_class, sample_class
