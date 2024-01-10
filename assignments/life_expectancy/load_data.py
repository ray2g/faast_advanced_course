"""Module to load data."""

# import libraries
import numpy as np
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