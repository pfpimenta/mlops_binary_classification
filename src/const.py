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
X_DATA_COLUMNS = ["Time"] + ["V" + str(i) for i in range(1, 29)] + ["Amount"]
X_DATA_DTYPES = [np.dtype("float64") for col in X_DATA_COLUMNS]
RAW_DATA_COLUMNS = ["Time"] + ["V" + str(i) for i in range(1, 29)] + ["Amount", "Class"]
RAW_DATA_DTYPES = X_DATA_DTYPES + [np.dtype("int64")]
