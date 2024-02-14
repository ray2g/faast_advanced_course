"""Module to load data."""

# import libraries
import pandas as pd

from pathlib import Path
from typing import Union
from pandas import DataFrame


def load_data(input_path: Union[str, Path], delimiter: str = "[\t,]") -> DataFrame:
    """
    Function wich loads the tsv file.

    :param inputh_path: The path where the tsv file is stored.
    :return df: Readed DataFrame.
    """
    print("\nLoading data...")

    return pd.read_csv(input_path, sep=delimiter, engine='python', index_col=False)

def load_json(input_path: Union[str, Path]) -> DataFrame:
    """
    Function which loads life expectancy json file as a DataFrame.

    :param input_path: The path where the json file is stored.
    : return DataFrame: Loaded json file as Pandas DataFrame.
    """
    print("\nLoading json file...")

    return pd.read_json(input_path, compression='zip', encoding='utf-8')
