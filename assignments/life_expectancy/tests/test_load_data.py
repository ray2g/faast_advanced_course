"""Test for the load_data module"""

import pandas as pd

from unittest.mock import patch
from life_expectancy.context import Context, ConcreteTsvStrategy, ConcreteJsonStrategy


def test_load_data(eu_life_expectancy_tsv):
    """Verify the function can load the tsv data from the fixture."""
    # Patch the `read_csv()` function with the mocked one
    with patch("life_expectancy.load_data.pd.read_csv") as mock_read_csv:
        # Define what read_csv should return
        mock_read_csv.return_value = pd.DataFrame()
        # Call the loader method and assert the mocked function was called
        context = Context()
        context.set_strategy(ConcreteTsvStrategy())
        context._strategy.loader(eu_life_expectancy_tsv)
        mock_read_csv.assert_called_once_with(eu_life_expectancy_tsv, sep="[\t,]", engine="python", index_col=False)

def test_load_json(eu_life_expectancy_json):
    """Verify the function can load the json data from the fixture."""
    # Patch the `read_json()` function with the mocked one
    with patch("life_expectancy.load_data.pd.read_json") as mock_read_json:
        # Define what read_json should return
        mock_read_json.return_value = pd.DataFrame()
        # Call the `load_json()` function and assert the mocked function was called
        context = Context()
        context.set_strategy(ConcreteJsonStrategy())
        context._strategy.loader(eu_life_expectancy_json)
        mock_read_json.assert_called_once_with(eu_life_expectancy_json, compression='zip', encoding='utf-8')