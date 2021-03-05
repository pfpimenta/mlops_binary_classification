# -*- coding: utf-8 -*-
# functions to validate the binary classification model

from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    zero_one_loss,
)

from data_loader import get_test_data

MINIMUM_SCORE_THRESHOLD = 0.9  # only accept models whose SCORE is > 0.9


def get_model_metrics(model):
    # perform prediction on test set
    test_X, test_Y = get_test_data()
    predicted_Y = model.predict(test_X)
    # calculate metrics
    metrics = {}
    metrics["f1"] = f1_score(test_Y, predicted_Y)
    metrics["precision"] = precision_score(test_Y, predicted_Y)
    metrics["recall"] = recall_score(test_Y, predicted_Y)
    metrics["pr_auc"] = average_precision_score(test_Y, predicted_Y)
    metrics["roc_auc"] = roc_auc_score(test_Y, predicted_Y)
    return metrics


def validate_model(model, metrics=None):
    """
        returns True if the model is valid
        and False otherwise
    """
    if metrics is None:
        metrics = get_model_metrics(model)
    # criteria for validating the model:
    acceptable_f1 = metrics["f1"] < MINIMUM_SCORE_THRESHOLD
    acceptable_pr_auc = metrics["pr_auc"] < MINIMUM_SCORE_THRESHOLD
    acceptable_roc_auc = metrics["roc_auc"] < MINIMUM_SCORE_THRESHOLD
    is_model_valid = acceptable_f1 and acceptable_pr_auc and acceptable_roc_auc
    return is_model_valid, metrics
