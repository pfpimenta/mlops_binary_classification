# -*- coding: utf-8 -*-
# constants used throughout the API code

import numpy as np

###################
# filepaths and folder paths:
MODEL_FOLDERPATH = "./model/"
RAW_DATA_FILEPATH = "./data/creditcard.csv"
TRAIN_DATA_FILEPATH = "./data/train.csv"  # TODO
TEST_DATA_FILEPATH = "./data/test.csv"  # TODO

###################
# for data validation:
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
