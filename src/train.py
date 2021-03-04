# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier

from data_loader import get_test_data, get_training_data


def train_model():
    train_X, train_Y = get_training_data()
    model = RandomForestClassifier(random_state=0)
    model.fit(train_X, train_Y)
    return model


def evaluate_model(model) -> float:
    test_X, test_Y = get_testdata()
    score = model.score(test_X, test_Y)
    return score


def train():
    model = train_model()
    score = evaluate_model(model)
    return model, score
