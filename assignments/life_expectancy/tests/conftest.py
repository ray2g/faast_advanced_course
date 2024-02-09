"""Pytest configuration file - Fixture Definition"""

import pandas as pd
import pytest
from pathlib import Path
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
    """tsv file path"""
    return f"{FIXTURES_DIR}/eu_life_expectancy_raw.tsv"

@pytest.fixture(scope="session")
def expected_regions() -> DataFrame:
    """Fixture that defines the expected regions
       to be considered by the region filter.
    """
    return [
    'AT','FI','ES','EL','EE','DK','DE','CZ','CY','CH','BG','BE','FX','SK','SI',\
    'SE','RO','PT','PL','NO','NL','LU','LT','IT','UK','IS','HU','IE','MT','MK','LI',\
    'FR','RS','HR','LV','UA','TR','ME','AL','AZ','GE','BY','AM','MD','SM','RU','XK'
    ]

@pytest.fixture()
def eu_life_expect_json() -> DataFrame:
    """Fixture to load the expected raw data from json file"""
    return pd.read_json(FIXTURES_DIR/"eurostat_life_expect.zip", compression='zip', encoding='utf-8')

@pytest.fixture()
def eu_life_expectancy_json() -> DataFrame:
    """Fixture with the expected path to load eurostat_life_expect json zipped file"""
    return f"{FIXTURES_DIR}/eurostat_life_expect.zip"
