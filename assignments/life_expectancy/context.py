"""Context Interface and Strategies"""

# import libraries
from enum import Enum
from pathlib import Path
from typing import Union
from pandas import DataFrame
from abc import ABC, abstractmethod
from life_expectancy.load_data import load_data, load_json
from life_expectancy.cleaning import clean_data, clean_data_json
from life_expectancy.save_data import save_data


class Strategy(ABC):
    """
    Strategy interface which declares the common operations.
    """

    @abstractmethod
    def loader(self, path: Union[str, Path]):
        pass

    @abstractmethod
    def cleaner(self, df: DataFrame, region_filter: Enum):
        pass

    @abstractmethod
    def saver(self, df: DataFrame, path: Union[str, Path]):
        pass

"""
Concrete Strategies implementing the methods following the base Strategy Interface.
"""

class ConcreteTsvStrategy(Strategy):
    def loader(self, path) -> DataFrame:
        return load_data(input_path=path)
    
    def cleaner(self, df: DataFrame, region_filter: Enum) -> DataFrame:
        return clean_data(df, region=region_filter)
        
    def saver(self, df: DataFrame, path: Union[str, Path]) -> None:
        return save_data(df, output_path=path)
    
class ConcreteJsonStrategy(Strategy):
    def loader(self, path) -> DataFrame:
        return load_json(input_path=path)
    
    def cleaner(self, df: DataFrame, region_filter: Enum) -> DataFrame:
        return clean_data_json(df, region=region_filter)
        
    def saver(self, df: DataFrame, path: Union[str, Path]) -> None:
        return save_data(df, output_path=path)
    
class Context():
    """
    Class which implements the Context object.
    It defines the interface for the defined strategies.
    """

    def __init__(self) -> None:
        """Init Context object."""
        self._strategy = Strategy

    def set_strategy(self, strategy: Strategy) -> None:
        """Allowing the Context to define the strategy object."""
        self._strategy = strategy

    def get_strategy(self) -> None:
        """Allowing the Context to get the strategy object."""
        return self._strategy

    def data_workflow(
                    self,
                    input_path: Union[str, Path],
                    region: Enum,
                    output_path: Union[str, Path]
                    ) -> None:
        """Steps to load, clean, and save the data."""

        df = self._strategy.loader(path=input_path)
        clean_df = self._strategy.cleaner(df, region_filter=region)
        self._strategy.saver(clean_df, path=output_path)
