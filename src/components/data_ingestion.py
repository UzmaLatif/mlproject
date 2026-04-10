import os
import pandas as pd
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

class DataIngestion:
    def __init__(self):
        ROOT_DIR = os.getcwd()  # project root
        self.artifact_dir = os.path.join(ROOT_DIR, "artifact")
        os.makedirs(self.artifact_dir, exist_ok=True)
        
      
        self.train_path = os.path.join(self.artifact_dir, "train.csv")
        self.test_path = os.path.join(self.artifact_dir, "test.csv")
        self.data_path = os.path.join(self.artifact_dir, "data.csv")  # NEW
    

    def initiate_data_ingestion(self):
        print("📥 Starting Data Ingestion")
        if not os.path.exists(self.train_path) or not os.path.exists(self.test_path):
            raise FileNotFoundError("Train or Test CSV not found in artifact folder!")

        print(f"Train CSV path: {self.train_path}")
        print(f"Test CSV path: {self.test_path}")
        print("✅ Data Ingestion completed")
        return self.train_path, self.test_path, self.data_path
if __name__ == "__main__":
    print("🔥 PIPELINE STARTED")

    # 1️⃣ Data Ingestion
    from src.components.data_ingestion import DataIngestion
    from src.components.data_transformation import DataTransformation
    from src.components.model_trainer import ModelTrainer

    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    # 2️⃣ Data Transformation
    data_transform = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transform.initiate_data_transformation(
        train_path, test_path
    )
    print("✅ Data Transformation completed")
    print("Preprocessor saved at:", preprocessor_path)

    # 3️⃣ Model Training
    modeltrainer = ModelTrainer()
    print("🚀 Starting Model Training")
    r2_score = modeltrainer.initiate_model_trainer(train_arr, test_arr, preprocessor_path)
    print(f"✅ Model Training Completed. R2 Score: {r2_score}")
