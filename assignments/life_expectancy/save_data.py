"""Module to load data."""

# import libraries
from pathlib import Path
from typing import Union
from pandas import DataFrame


def save_data(df: DataFrame, output_path: Union[str, Path]) -> None:
    """
    Function which saves a dataframe as csv.

    param: df: The input dataframe to be saved.
    param output_path: The path where the dataframe will be saved.
    """
    # save dataframe as csv
    df.to_csv(output_path, index=False)

    print(f"\nProcess Finished! The file was saved as csv in:  {output_path}\n")