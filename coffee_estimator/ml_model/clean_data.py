import pandas as pd
import numpy as np
from . import views
from .models import Coffee


def clean_data ():
    df = Coffee.objects.all


    object_columns = ['Species', 'Country.of.Origin', 'Region', 'Company', 'Variety', 'Processing.Method']

    # Iterate through each object column and one-hot encode it
    for column in object_columns:
        df = pd.concat([df.drop(column, axis=1), pd.get_dummies(df[column]).add_prefix(f'{column}_')], axis=1)


    df_c = pd.read_csv('test_x25.csv')

    new_columns = set(df_c.columns) - set(df.columns)


    zero_data = {col: [False] * len(df_c) for col in new_columns}  # assuming length of df1 is the target length
    new_df = pd.DataFrame(zero_data)

    # Concatenate the original df1 with the new columns DataFrame
    df_to_pred = pd.concat([df, new_df], axis=1)


    df_to_pred.dropna()


    correct_feature_order = df_c.columns


    df_to_pred = df_to_pred[correct_feature_order]

