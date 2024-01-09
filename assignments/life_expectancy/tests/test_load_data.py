"""Test for the load_data module"""

import pandas as pd

from unittest.mock import patch
from life_expectancy.load_data import load_data


def test_load_data(eu_life_expectancy_tsv):
    """Verify the function can load the data from the fixture."""
    # Patch the `read_csv()` function with the mocked one
    with patch("life_expectancy.load_data.pd.read_csv") as mock_read_csv:
        # Define what read_csv should return
        mock_read_csv.return_value = pd.DataFrame()
        # Call the `load_data()` function and assert the mocked function was called
        load_data(eu_life_expectancy_tsv)
        mock_read_csv.assert_called_once_with(eu_life_expectancy_tsv, sep="[\t,]", engine="python", index_col=False)