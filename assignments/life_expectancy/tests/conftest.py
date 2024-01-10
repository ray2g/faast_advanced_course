"""Pytest configuration file - Fixture Definition"""

import pandas as pd
import pytest

from pandas import DataFrame
from . import FIXTURES_DIR


@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> DataFrame:
    """Fixture to load the raw input of the cleaning script
    AKA sample
    """
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv", sep="[\t,]", engine="python")

@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected input of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv", engine="python")

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv", sep="[\t,]", engine="python")

@pytest.fixture(scope="session")
def eu_life_expectancy_tsv():
    """tsv file path."""
    return f"{FIXTURES_DIR}/eu_life_expectancy_raw.tsv"
