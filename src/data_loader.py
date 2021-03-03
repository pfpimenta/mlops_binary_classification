# -*- coding: utf-8 -*-
# functions to generate balanced dataset from raw data

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# TODO
def get_training_data():
    pass


# TODO
def get_test_data():
    pass


def normalize_col(col):
    """ normalizes a pandas dataframe column values between 0 and 1 """
    normalized_col = (col - col.min()) / (col.max() - col.min()).astype(np.float64)
    return normalized_col


def generate_dataset():
    # TODO
    # load raw csv
    raw_data = pd.read_csv("./data/creditcard.csv")

    # separate positive and negative class rows
    positive_rows = raw_data.loc[raw_data["Class"] == 1].copy()
    negative_rows = raw_data.loc[raw_data["Class"] == 0].copy()

    # normalize time and amount columns
    # positive_rows['Time'] = normalize_col(positive_rows['Time'])
    # positive_rows['Amount'] = normalize_col(positive_rows['Amount'])
    # negative_rows['Time'] = normalize_col(negative_rows['Time'])
    # negative_rows['Amount'] = normalize_col(negative_rows['Amount'])

    # continuous multivariable stratified sampling
    # cols = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    #     'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    #    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
    cols = ["V1", "V2", "V3", "V4", "V5"]
    for col in cols:
        col_name = col + "_strat"
        print("DEBUG " + col_name)
        positive_rows[col_name] = pd.qcut(
            normalize_col(positive_rows[col]), q=2, labels=["A", "B"]
        )
        print(positive_rows[col_name].value_counts())
    stratify_cols = [col + "_strat" for col in cols]
    pos_train, pos_test = train_test_split(
        positive_rows,
        test_size=0.3,
        random_state=5,
        stratify=positive_rows[stratify_cols],
    )

    # drop these columns that were created only to split the data in train / test
    pos_train = pos_train.drop(columns=stratify_cols)
    pos_test = pos_test.drop(columns=stratify_cols)

    print(pos_train.head())
    print(pos_train.shape)

    # TODO samplear do neg esse mesmo numero (undersample)
    num_pos_train = pos_train.shape[0]

    # linhas 1:
    #     70% vai pro csv de treino = 344
    #         dai SMOTE pra criar 20% disso: + 68
    #         dai duplicar: (344+68)*2 = 824
    #     30% vai pro csv de teste = 148
    # linhas 0:
    #     sampleia de acordo com as distribuiçoes
    #     824 samples pra treino
    #     148 samples pra teste
    #     (sem repetiçao entre os conjuntos)
