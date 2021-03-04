# -*- coding: utf-8 -*-
# functions to validate data

from collections import Counter

import numpy as np
import pandas as pd

RAW_DATA_COLUMNS = [
    "Time",
    "V1",
    "V2",
    "V3",
    "V4",
    "V5",
    "V6",
    "V7",
    "V8",
    "V9",
    "V10",
    "V11",
    "V12",
    "V13",
    "V14",
    "V15",
    "V16",
    "V17",
    "V18",
    "V19",
    "V20",
    "V21",
    "V22",
    "V23",
    "V24",
    "V25",
    "V26",
    "V27",
    "V28",
    "Amount",
    "Class",
]
RAW_DATA_DTYPES = [
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("int64"),
]
X_DATA_COLUMNS = [
    "Time",
    "V1",
    "V2",
    "V3",
    "V4",
    "V5",
    "V6",
    "V7",
    "V8",
    "V9",
    "V10",
    "V11",
    "V12",
    "V13",
    "V14",
    "V15",
    "V16",
    "V17",
    "V18",
    "V19",
    "V20",
    "V21",
    "V22",
    "V23",
    "V24",
    "V25",
    "V26",
    "V27",
    "V28",
    "Amount",
]
X_DATA_DTYPES = [
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
    np.dtype("float64"),
]


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
