"""Test for the save_data module"""

import pandas
from pandas import DataFrame
from life_expectancy.save_data import save_data
from unittest.mock import patch
from . import OUTPUT_DIR

def test_save_data(eu_life_expectancy_expected: DataFrame) -> None:
    """
    Test save_data module with mock
    :param eu_life_expectancy_expected: Input DataFrame to be saved
    """
    with patch("pandas.DataFrame.to_csv") as to_csv_mock:
        to_csv_mock.side_effect = print(f"\nProcess Finished! \
                                            The file was saved as csv in: \
                                            {OUTPUT_DIR}/pt_life_expectancy_obtained.csv")
        
        save_data(eu_life_expectancy_expected,f"{OUTPUT_DIR}/pt_life_expectancy_obtained.csv")
        to_csv_mock.assert_called_once()