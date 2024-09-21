import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

# Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a given file."""
        pass

# Implement a concrete class for ZIP Ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extracts a .zip file and returns the content as a pandas DataFrame."""
        # Ensure the file is a .zip
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file.")
        
        # Logic to extract the zip file and read data
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Assuming there's only one file in the zip and it's a CSV
             zip_ref.extractall("extracted_data")
            
        extracted_files = os.listdirn("extracted_data")
        csv_file = [file for file in extracted_files if file.endswith(".csv")]

        if len(csv_file) == 0:
            raise FileNotFoundError("No CSV file found in the etracted data.")
        
        if len(csv_file) > 1:
            raise ValueError("Multiple CSV files found in the extracted data. specify the file to read.")
        
        csv_file_path= os.path.join("extracted_data", csv_file[0])
        df = pd.read_csv(csv_file_path)

        return df
    


# Implement a factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Factory method to create a DataIngestor based on the file type."""
        if file_extension ==".zip":
            return ZipDataIngestor()
        else:
            raise ValueError("Unsupported file type. Only .zip files are supported.") 
        
if __name__ == "__main__":
    # Use the factory to create a DataIngestor
    file_path= "C:\Users\Khalifa\Desktop\AI-project\prices-predictor\data\archive.zip"
    
    file_extension= os.path.splitext(file_path)[1]

    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    df = data_ingestor.ingest(file_path)

    print(df.head())
    
