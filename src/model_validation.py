# -*- coding: utf-8 -*-
# functions to validate the binary classification model

from data_loader import get_test_data

MINIMUM_SCORE_THRESHOLD = 0.9  # only accept models whose score is > 0.9


def evaluate_model(model) -> float:
    test_X, test_Y = get_test_data()
    score = model.score(test_X, test_Y)
    return score


def validate_model(model):
    """
        returns True if the model is valid
        and False otherwise
    """
    score = evaluate_model(model)
    if score < MINIMUM_SCORE_THRESHOLD:
        return False, score

    return True, score
