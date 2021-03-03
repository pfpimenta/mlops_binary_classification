# -*- coding: utf-8 -*-
# functions to generate balanced dataset from raw data

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


def get_training_data():
    """ TODO doc
    """
    # TODO
    pass


def get_test_data():
    """ TODO doc
    """
    # TODO
    pass


def normalize_col(col):
    """ normalizes a pandas dataframe column values between 0 and 1 """
    normalized_col = ((col - col.min()) / (col.max() - col.min())).astype(np.float64)
    return normalized_col


def continuous_multivar_stratified_split(df, test_size=0.3):
    """ TODO doc
    """
    cols = ["V1", "V2", "V3", "V4", "V5"]
    for col in cols:
        col_name = col + "_strat"
        # print("DEBUG " + col_name)
        print(df[col].head())
        print(df[col].shape)
        normalized_col = normalize_col(df[col])
        print(normalized_col.head())
        print(normalized_col.shape)
        df[col_name] = pd.qcut(normalized_col, q=2, labels=["A", "B"])
        # print(df[col_name].value_counts())
    stratify_cols = [col + "_strat" for col in cols]
    df_train, df_test = train_test_split(
        df, test_size=test_size, random_state=5, stratify=df[stratify_cols]
    )
    # drop these columns that were created only to split the data in train / test
    df_train = df_train.drop(columns=stratify_cols)
    df_test = df_test.drop(columns=stratify_cols)

    return df_train, df_test


def generate_dataset():

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

    # train/test split
    pos_train, pos_test = continuous_multivar_stratified_split(positive_rows)

    num_pos_train_samples = pos_train.shape[0]
    num_pos_test_samples = pos_test.shape[0]
    num_neg_train_samples = num_pos_train_samples * 2
    num_neg_test_samples = num_pos_test_samples
    num_neg_samples = num_neg_train_samples + num_pos_test_samples
    print(
        f"DEBUG {num_pos_train_samples}, {num_pos_test_samples}, {num_neg_train_samples}, {num_neg_samples}"
    )

    # TODO mudar? talvez usar algum sampling nao aleatorio
    neg_samples = negative_rows.sample(n=num_neg_samples, random_state=1)
    neg_train, neg_test = continuous_multivar_stratified_split(
        neg_samples, test_size=num_pos_test_samples
    )

    # DEBUG
    # print(pos_train.head())
    # print(pos_train.shape)

    # apply SMOTE on training positive samples
    # pos_train_X = pos_train.drop(columns=['Class'])
    # pos_train_X, pos_train_y = SMOTE().fit_resample(pos_train_X, pos_train['Class'])

    # DEBUG
    # print(pos_train_X.head())
    # print(pos_train_X.shape)

    train_samples = pd.concat([pos_train, neg_train])
    test_samples = pd.concat([pos_test, neg_test])
    return train_samples, test_samples

    # TODO samplear do neg esse mesmo numero (undersample)

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
