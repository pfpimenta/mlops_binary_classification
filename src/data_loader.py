# -*- coding: utf-8 -*-
# functions to generate balanced dataset from raw data

from math import floor
from random import randint

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

from const import RAW_DATA_FILEPATH, TEST_DATA_FILEPATH, TRAIN_DATA_FILEPATH
from data_validation import validate_raw_data

# flag to avoid generating test and train datasets more than once
is_dataset_ready = False


def get_one_sample():
    test_X, test_Y = get_test_data()
    sample = test_X.head(1)
    sample_class = int(test_Y.head(1).values[0])
    return sample, sample_class


def get_random_sample():
    test_X, test_Y = get_test_data()
    num_rows = len(test_X.index)
    random_index = randint(0, num_rows - 1)
    sample = test_X.head(random_index)
    sample_class = int(test_Y.head(random_index).values[0])
    return sample, sample_class


def get_training_data():
    if is_dataset_ready is False:
        train_df, _ = generate_test_and_train_sets()
    else:
        # load from csv
        train_df = pd.read_csv(TRAIN_DATA_FILEPATH)
    # separate on X and Y
    train_X = train_df.drop(columns=["Class"])
    train_Y = train_df["Class"]
    return train_X, train_Y


def get_test_data():
    if is_dataset_ready is False:
        _, test_df = generate_test_and_train_sets()
    else:
        # load from csv
        test_df = pd.read_csv(TEST_DATA_FILEPATH)
    # separate on X and Y
    test_X = test_df.drop(columns=["Class"])
    test_Y = test_df["Class"]
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
        df, test_size=test_size, random_state=0, stratify=df[stratify_cols]
    )

    # drop these columns that were created only to split the data in train / test
    df_train = df_train.drop(columns=stratify_cols)
    df_test = df_test.drop(columns=stratify_cols)

    return df_train, df_test


def get_test_and_train_sets():
    """
        This function returns the X and Y of the train and test datasets.
        For this, it uses undersampling and oversampling in order to balance
        the positive and negative sample quantities.

            original dataset:
            - 492 positive samples
            - 284315 negative samples
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

    # train/test split
    pos_train, pos_test = continuous_multivar_stratified_split(positive_rows)

    # setup positive and negative sample quantities
    num_pos_rows = len(positive_rows.index)
    num_neg_rows = len(negative_rows.index)
    class_imbalance = num_neg_rows / num_pos_rows
    num_pos_train_samples = pos_train.shape[0]
    num_pos_test_samples = pos_test.shape[0]
    num_neg_train_samples = num_pos_train_samples * 2
    num_neg_test_samples = floor(num_pos_test_samples * class_imbalance)
    num_neg_samples = num_neg_train_samples + num_neg_test_samples

    # undersample negative samples
    # (tries to keep in the test set the same class imbalance found in the raw data)
    neg_samples = negative_rows.sample(n=num_neg_samples, random_state=0)
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

    # apply SMOTE on training samples (oversampling)
    # (solve class imbalance by creating new samples base on interpolations)
    train_X, train_Y = SMOTE(random_state=0).fit_resample(train_X, train_Y)

    return train_X, train_Y, test_X, test_Y


def generate_test_and_train_sets():
    """
        generates train and test sets from the raw data csv
        and saves them in separate csv files
    """
    global is_dataset_ready

    # get train and test data
    train_X, train_Y, test_X, test_Y = get_test_and_train_sets()
    train_df = train_X
    train_df["Class"] = train_Y
    test_df = test_X
    test_df["Class"] = test_Y

    # save to csv
    train_df.to_csv(TRAIN_DATA_FILEPATH, index=False)
    test_df.to_csv(TEST_DATA_FILEPATH, index=False)

    is_dataset_ready = True

    return train_df, test_df
