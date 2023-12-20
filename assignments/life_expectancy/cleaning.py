# Script to clean data/life_expectancy_raw.tsv ___//

# import libraries
import io
import csv
import argparse
import pandas as pd
import numpy as np

from io import TextIOWrapper
from pandas import DataFrame
from pathlib import Path
from typing import Union




def load_data(input_path: Union[str, Path]) -> TextIOWrapper:
    """
    Function wich loads the tsv file.

    :param inputh_path: The path where the tsv file is stored.
    :return data: Readed data object.
    """
    print("\nLoading data...")

    # open and read raw data file
    with open(input_path, 'r', encoding="utf8") as raw_data:
        data = raw_data.read()

    return data


def clean_data(data, region:str) -> DataFrame:
    '''
    Function which cleans a data object by:

    - Replacing "," with '\t'
    - Replacing ":" with NaN values
    - Renaming column "geo\time" for "region"
    - Transforms the tsv to dataframe
    - unpivot the dataframe
    - removing characters from value column
    - converting columns to the respetive type
    - dropping the null values
    - filtering the dataframe by region

    :param data: tsv data object to be cleaned and filtered.
    :return df_clean: The clean tsv file as dataframe.
    '''

    print("\nCleaning the tsv file...\n")

    # replace ',' with '\t' values in 
    data_clear = data.replace(',' , '\t')

    # Create a StringIO object
    # which stores data in memory
    data_buffer = io.StringIO(data_clear)

    # Read the TSV data into a list of lists
    tsv_data = []
    for row in csv.reader(data_buffer, delimiter='\t'):
        tsv_data.append(row)

    # transform into dataframe 
    df = pd.DataFrame(tsv_data[1:], columns=tsv_data[0])

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
    df_clean_filt = df_clean[df_clean["region"] == region]
    
    return df_clean_filt


def save_data(df: DataFrame, output_path: Union[str, Path]) -> None:
    """
    Function which saves a dataframe as csv.

    param: df: The input dataframe to be saved.
    param output_path: The path where the dataframe will be saved.
    """
    # save dataframe as csv
    df.to_csv(output_path, index=False)

    print(f"Process Finished! The file was saved as csv in:\n{output_path}\n")


def main(): # pragma: no cover
    """
    Main function which config the arparse and
    calls the functions to load, clean and save the tsv file.

    Functions description:
    - load_data: Function wich loads the tsv file.
    - clean_data: Function which cleans a data object by:
                  replacing "," with '\t',
                  replacing ":" with NaN values,
                  renaming column "geo\time" for "region",
                  transforms the tsv to dataframe,
                  unpivot the dataframe,
                  removing characters from value column,
                  converting columns to the respetive type,
                  dropping the null values,
                  filtering the dataframe by region.
    - save_data: Function which saves a dataframe as csv.
    """
    
    # config argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help= "Input file path.") 
    parser.add_argument('-o', help = "Output file path.")
    parser.add_argument("-r", default="PT", help = "Desire region to filter the csv.")
    args = parser.parse_args()

    # Check if all required arguments are provided
    required_args = ["-i", "-o"]
    for arg in required_args:
        if arg not in args:
            raise Exception(f"Missing argument: '{arg}'")

    # read tsv file
    data = load_data(args.i)
    # clean tsv file
    df = clean_data(data, args.r)
    # save dataframe as csv
    save_data(df, args.o)

if __name__ == "__main__":  # pragma: no cover
    main()       
