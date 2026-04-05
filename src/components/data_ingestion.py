import os
import pandas as pd
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

class DataIngestion:
    def __init__(self):
        # Paths for train/test CSVs inside src/artifact
        self.train_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "artifact",
            "train.csv"
        )
        self.test_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "artifact",
            "test.csv"
        )

    def initiate_data_ingestion(self):
        print("📥 Starting Data Ingestion")
        if not os.path.exists(self.train_path) or not os.path.exists(self.test_path):
            raise FileNotFoundError("Train or Test CSV not found in artifact folder!")

        print(f"Train CSV path: {self.train_path}")
        print(f"Test CSV path: {self.test_path}")
        print("✅ Data Ingestion completed")
        return self.train_path, self.test_path

if __name__ == "__main__":
    print("🔥 MAIN STARTED")

    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    data_transform = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transform.initiate_data_transformation(
    train_path, test_path
    )

    print("✅ Data Transformation completed")
    print("Preprocessor saved at:", preprocessor_path)

    modeltrainer=ModelTrainer()
    modeltrainer.initiate_model_trainer(train_arr, test_arr, preprocessor_path)
    print("🚀 Starting Model Training")
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr, preprocessor_path))


