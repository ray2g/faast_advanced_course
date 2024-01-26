"""Module to clean data."""

# import libraries
import numpy as np
import pandas as pd

from pandas import DataFrame
from life_expectancy.regions import Region


def clean_data(df: DataFrame, region: Region) -> DataFrame:
    '''
    Function which cleans a DataFrame by:

    - Replacing ":" with NaN values
    - Renaming column "geo\time" for "region"
    - unpivot the dataframe
    - removing characters from value column
    - converting columns to the respetive type
    - dropping the null values
    - filtering the dataframe by region

    :param data: DataFrame to be cleaned and filtered.
    :return DataFrame: The clean dataframe.
    '''

    print("\nCleaning data...")
    
    # rename "geo\time" column with "region"
    df.columns.values[3] = 'region'

    # replace ":" as NaN
    df_replaced_nulls = df.replace(to_replace=':.*', value=np.nan, regex=True)
    
    # unpivot dataframe
    df_unpivot = pd.melt(
                    df_replaced_nulls, 
                    id_vars=list(df_replaced_nulls.iloc[:, :4].columns),
                    value_vars=list(df_replaced_nulls.iloc[:, 4:].columns),
                    var_name='year'
                )
    
    # remove strings from value column
    df_unpivot['value'] = df_unpivot['value'].str.replace('[^\d\-+\.]', '', regex=True)
    
    # convert value column into float
    df_unpivot['value'] = df_unpivot['value'].apply(pd.to_numeric, errors="raise")

    # convert "year" column to integer
    df_unpivot['year'] = df_unpivot['year'].astype(int)

    # drop nulls from "value" column
    df_clean = df_unpivot.dropna()

    # filter dataframe by desire region
    df_clean_filt = df_clean[df_clean['region'] == region.value]

    return df_clean_filt


