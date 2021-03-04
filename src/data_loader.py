# -*- coding: utf-8 -*-
# functions to generate balanced dataset from raw data

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

from data_validation import validate_raw_data

RAW_DATA_FILEPATH = "./data/creditcard.csv"
TRAIN_DATA_FILEPATH = "./data/train.csv"  # TODO
TEST_DATA_FILEPATH = "./data/test.csv"  # TODO


def get_one_sample():
    test_X, test_Y = get_test_data()
    sample = test_X.head(1)
    sample_class = test_Y.head(1).values[0]
    return sample, sample_class


def get_training_data():
    train_X, train_Y, _, _ = generate_dataset()
    return train_X, train_Y


def get_test_data():
    _, _, test_X, test_Y = generate_dataset()
    return test_X, test_Y


def normalize_col(col):
    """ normalizes a pandas dataframe's column values between 0 and 1 """
    normalized_col = ((col - col.min()) / (col.max() - col.min())).astype(np.float64)
    return normalized_col


def continuous_multivar_stratified_split(df, test_size=0.3):
    """
        Splits the input dataframe into train and test using some of the
        continuous feature variables to minimize distribution difference
        between train and test sets.
    """
    # using 5 variables because it is the maximum that works
    cols = ["V1", "V2", "V3", "V4", "V5"]

    # discretize variable using 2 bins
    for col in cols:
        col_name = col + "_strat"
        normalized_col = normalize_col(df[col])
        df[col_name] = pd.qcut(normalized_col, q=2, labels=["A", "B"])

    # use discrete version of mutivariable stratified split
    stratify_cols = [col + "_strat" for col in cols]
    df_train, df_test = train_test_split(
        df, test_size=test_size, random_state=5, stratify=df[stratify_cols]
    )

    # drop these columns that were created only to split the data in train / test
    df_train = df_train.drop(columns=stratify_cols)
    df_test = df_test.drop(columns=stratify_cols)

    return df_train, df_test


def generate_dataset():
    """
        This function returns the X and Y of the train and test datasets.
        For this, it uses undersampling and oversampling in order to balance
        the positive and negative sample quantities.

            test set:
            - 148 positive samples
            - 148 negative samples
            train set:
            - 688 positive samples
                - 344 from CSV file
                - 344 created using SMOTE oversampling
            - 688 negative samples
    """
    # load raw csv
    raw_data = pd.read_csv(RAW_DATA_FILEPATH)

    # checks if data is valid
    is_data_valid = validate_raw_data(raw_data)
    if is_data_valid == False:
        raise Exception("Loaded raw data is not valid")

    # separate positive and negative class rows
    positive_rows = raw_data.loc[raw_data["Class"] == 1].copy()
    negative_rows = raw_data.loc[raw_data["Class"] == 0].copy()

    # normalize time and amount columns
    # positive_rows['Time'] = normalize_col(positive_rows['Time'])
    # positive_rows['Amount'] = normalize_col(positive_rows['Amount'])
    # negative_rows['Time'] = normalize_col(negative_rows['Time'])
    # negative_rows['Amount'] = normalize_col(negative_rows['Amount'])

    # train/test split
    pos_train, pos_test = continuous_multivar_stratified_split(positive_rows)

    # setup positive and negative sample quantities
    num_pos_train_samples = pos_train.shape[0]
    num_pos_test_samples = pos_test.shape[0]
    num_neg_train_samples = num_pos_train_samples * 2
    num_neg_test_samples = num_pos_test_samples
    num_neg_samples = num_neg_train_samples + num_pos_test_samples

    # undersample negative samples
    neg_samples = negative_rows.sample(n=num_neg_samples, random_state=1)
    neg_train, neg_test = continuous_multivar_stratified_split(
        neg_samples, test_size=num_pos_test_samples
    )

    # gather positive and negative samples
    test_samples = pd.concat([pos_test, neg_test])
    train_samples = pd.concat([pos_train, neg_train])

    # separate on X and Y
    train_X = train_samples.drop(columns=["Class"])
    train_Y = train_samples["Class"]
    test_X = test_samples.drop(columns=["Class"])
    test_Y = test_samples["Class"]

    # apply SMOTE on training samples
    # (solve class imbalance by creating new samples base on interpolations)
    train_X, train_Y = SMOTE().fit_resample(train_X, train_Y)

    return train_X, train_Y, test_X, test_Y
