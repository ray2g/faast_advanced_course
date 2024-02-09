"""Tests for the cleaning module"""


import pandas as pd
from life_expectancy.context import Context, ConcreteTsvStrategy, ConcreteJsonStrategy
from life_expectancy.regions import Region
from pandas import DataFrame


def test_clean_data(eu_life_expectancy_raw: DataFrame, eu_life_expectancy_expected: DataFrame
    ) -> None:
    """
    Tests the clean_data module comparing the output with an expected output.

    :param eu_life_expectancy_raw: Tsv sampled Dataframe.
    :param eu_life_expectancy_expected: Expected DataFrame.
    """
    context = Context()
    context.set_strategy(ConcreteTsvStrategy())
    eu_life_expectancy_obtained = context._strategy.cleaner(eu_life_expectancy_raw, Region.PT).reset_index(drop=True)
    
    pd.testing.assert_frame_equal(
                        eu_life_expectancy_obtained,
                        eu_life_expectancy_expected
    )

def test_clean_data_json(eu_life_expect_json: DataFrame, pt_life_expectancy_expected: DataFrame
    ) -> None:
    """
    Tests the clean_data_json module comparing the output with an expected output.

    :param eu_life_expect_json: Json Dataframe.
    :param pt_life_expectancy_expected: Expected cleaned DataFrame.
    """
    context = Context()
    context.set_strategy(ConcreteJsonStrategy())
    eu_life_expectancy_obtained = context._strategy.cleaner(eu_life_expect_json, Region.PT).reset_index(drop=True)
    
    pd.testing.assert_frame_equal(
                        eu_life_expectancy_obtained,
                        pt_life_expectancy_expected
    )

