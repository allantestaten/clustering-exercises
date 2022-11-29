import pandas as pd
import numpy as np
from env import get_db_url
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
from sklearn.model_selection import train_test_split


# train test split from sklearn
from sklearn.model_selection import train_test_split
# imputer from sklearn
from sklearn.impute import SimpleImputer


def remove_columns(df, cols_to_remove):
    '''this function will drop columns selected from df'''
    df = df.drop(columns=cols_to_remove)
    return df

def handle_missing_values(df, prop_required_columns=0.5, prop_required_rows=0.75):
    '''this funciton will make sure to keep the given percentage of the data in each row and column'''
    column_threshold = int(round(prop_required_columns * len(df.index), 0))
    df = df.dropna(axis=1, thresh=column_threshold)
    row_threshold = int(round(prop_required_rows * len(df.columns), 0))
    df = df.dropna(axis=0, thresh=row_threshold)
    return df

def data_prep(df, col_to_remove=[], prop_required_columns=0.5, prop_required_rows=0.75):
    '''this function will remove columns and keep the requested amount of data in the df '''
    df = remove_columns(df, col_to_remove)
    df = handle_missing_values(df, prop_required_columns, prop_required_rows)
    return df