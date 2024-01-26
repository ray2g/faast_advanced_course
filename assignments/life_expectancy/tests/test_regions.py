"""Tests the Region Enum Module"""
# %%
from typing import List
from life_expectancy.regions import Region


def test_valid_regions(expected_regions) -> None:
    """
    Tests the 'considered_regions' classmethod of
    regions_enum module.

    :param expected_regions: Fixture which is a list of valid regions.
    """

    regions : List = Region.considered_regions()

    # Check if both lists of regions have the same number of elements
    assert len(regions) == len(expected_regions)
    
    # Check if both lists of regions have the same elements
    assert not set(regions) ^ set(expected_regions)