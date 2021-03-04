# -*- coding: utf-8 -*-
# functions to validate data

from collections import Counter

import pandas as pd

from const import RAW_DATA_COLUMNS, RAW_DATA_DTYPES, X_DATA_COLUMNS, X_DATA_DTYPES


def validate_raw_data(raw_data) -> bool:
    """
        returns True if the raw data is formatted as expected
        and False otherwise
    """
    are_columns_valid = list(raw_data.columns) == RAW_DATA_COLUMNS
    are_column_types_valid = list(raw_data.dtypes) == RAW_DATA_DTYPES
    is_raw_data_valid = are_columns_valid and are_column_types_valid
    return is_raw_data_valid


def validate_training_data(train_X, train_Y) -> bool:
    """
        returns True if the training data is formatted as expected
        and False otherwise
    """
    counter_train = Counter(train_Y)
    is_dataset_balanced = counter_train[0] == counter_train[1]
    are_columns_valid = list(train_X.columns) == X_DATA_COLUMNS
    are_column_types_valid = list(train_X.dtypes) == X_DATA_DTYPES
    is_data_valid = is_dataset_balanced and are_columns_valid and are_column_types_valid
    return is_data_valid


def validate_sample(sample) -> bool:
    """
        returns True if the sample is formatted as expected
        and False otherwise
    """
    is_dataframe = isinstance(sample, pd.DataFrame)
    are_columns_valid = list(sample.columns) == X_DATA_COLUMNS
    are_column_types_valid = list(sample.dtypes) == X_DATA_DTYPES
    is_sample_valid = is_dataframe and are_columns_valid and are_column_types_valid
    return is_sample_valid
