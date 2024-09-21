from abc import ABC, abstractmethod
import pandas as pd

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, pd: pd.DataFrame):
        """Abstract method to inspectt data from a given file."""
        pass


class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """Inspects the basic data types of the DataFrame."""
        print("\n Data Types and Non-nullInspection:")
        print(df.info())



class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """Inspects the summary statistics of the DataFrame."""
        print("\n Summary Statistics(categorical Features):")
        print(df.describe(include=["0"]))


class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        self.strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        return self.strategy.inspect(df)
    

if __name__ == "__main__":
    # Create a DataFrame

#   df= pd.read_csv("../extracted_data/AmesHousing.csv")

    inspector = DataInspector(DataTypesInspectionStrategy())
    
    
    # data = {
    #     "Name": ["Tom", "Nick", "John"],
    #     "Age": [20, 21, 19],
    #     "City": ["New York", "California", "Las Vegas"]
    # }
    # df = pd.DataFrame(data)

    # # Use the DataInspector with DataTypesInspectionStrategy
    # inspector = DataInspector(DataTypesInspectionStrategy())
    # inspector.execute_inspection(df)

    # # Use the DataInspector with SummaryStatisticsInspectionStrategy
    # inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    # inspector.execute_inspection(df)
