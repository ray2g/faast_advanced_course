"""Tests for the cleaning module"""


import pandas as pd
from life_expectancy.cleaning import clean_data
from life_expectancy.regions_enum import Region
from pandas import DataFrame


def test_clean_data(eu_life_expectancy_raw: DataFrame, eu_life_expectancy_expected: DataFrame
    ) -> None:
    """
    Tests the clean_data module comparing the output with an expected output.

    :param eu_life_expectancy_raw: Sampled Dataframe.
    :param eu_life_expectancy_expected: Expected DataFrame.
    """
    eu_life_expectancy_obtained = clean_data(eu_life_expectancy_raw, Region.PT).reset_index(drop=True)
    
    pd.testing.assert_frame_equal(
                        eu_life_expectancy_obtained,
                        eu_life_expectancy_expected
    )


