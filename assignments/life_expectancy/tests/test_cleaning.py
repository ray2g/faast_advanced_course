"""Tests for the cleaning module"""
from pathlib import Path
import pandas as pd

from life_expectancy.cleaning import load_data
from life_expectancy.cleaning import clean_data
from life_expectancy.cleaning import save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    input_path: Path = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
    output_path: Path = OUTPUT_DIR / "pt_life_expectancy.csv"
    

    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )

    # read tsv
    data = load_data(input_path)

    # clean tsv file
    df = clean_data(data, "PT")
    
    # save dataframe as csv
    save_data(df, output_path)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
