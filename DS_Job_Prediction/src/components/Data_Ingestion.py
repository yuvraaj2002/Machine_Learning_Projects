from src.logger import logging
from src.exception import CustomException
import sys
import os
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class Data_Ingestion_Config:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")


class Data_Ingestion:
    def __init__(self):
        self.data_paths = Data_Ingestion_Config()

    def initialize_data_ingestion(self, raw_data_path):
        try:
            logging.info("Data Ingestion initialized")

            # Let's first read the raw data from source
            df = pd.read_csv(raw_data_path)
            logging.info("Reading csv file completed successfully")

            # Let's now do the train test split
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=1)
            logging.info("Train test split done")

            # Let's make the directories to store the files
            os.makedirs(
                os.path.dirname(self.data_paths.train_data_path), exist_ok=True
            )

            # Let's now store the files
            train_data.to_csv(self.data_paths.train_data_path, index=False, header=True)
            test_data.to_csv(self.data_paths.test_data_path, index=False, header=True)
            logging.info("Files saved")

            logging.info("Data Ingestion completed")
            return (self.data_paths.train_data_path, self.data_paths.test_data_path)

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    data_ingestion_obj = Data_Ingestion()
    data_ingestion_obj.initialize_data_ingestion('notebook/Data.csv')