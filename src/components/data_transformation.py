import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.utils import save_object  # make sure this exists
import os

@dataclass
class DataTransformationConfig:
    # Preprocessor file path in root artifact folder
    preprocessor_obj_file_path = os.path.join(
        os.getcwd(),  # project root
        "artifact",
        "preprocessor.pkl"
    )

class DataTransformation:
    def __init__(self):
        # Configuration
        self.data_transformation_config = DataTransformationConfig()

        # Root artifact folder
        self.artifact_dir = os.path.join(os.getcwd(), "artifact")
        os.makedirs(self.artifact_dir, exist_ok=True)

        # Paths for saving artifacts
        self.preprocessor_path = os.path.join(self.artifact_dir, "preprocessor.pkl")
        self.data_csv_path = os.path.join(self.artifact_dir, "data.csv")  # combined dataset

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing score", "reading score"]
            categorical_columns = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course"
            ]

            # Numerical pipeline
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            # Categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder(handle_unknown='ignore')),
                ("scaler", StandardScaler(with_mean=False))
            ])

            print(f"Numerical columns: {numerical_columns}")
            print(f"Categorical columns: {categorical_columns}")

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor

        except Exception as e:
            print("Error in get_data_transformer_object:", e)
            raise e

    def initiate_data_transformation(self, train_path, test_path):
        try:
            print("🚀 Starting Data Transformation")

            # Read CSVs
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            print("✅ Train and Test CSVs read successfully")

            # Save combined dataset as data.csv
            full_df = pd.concat([train_df, test_df], axis=0)
            full_df.to_csv(self.data_csv_path, index=False)
            print("✅ data.csv saved at:", self.data_csv_path)

            # Preprocessing
            preprocessing_obj = self.get_data_transformer_object()
            target_column_name = "math score"

            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # Save preprocessor
            os.makedirs(os.path.dirname(self.preprocessor_path), exist_ok=True)
            print("📦 Saving preprocessor at:", self.preprocessor_path)
            save_object(file_path=self.preprocessor_path, obj=preprocessing_obj)
            print("✅ Preprocessor saved successfully!")

            return train_arr, test_arr, self.preprocessor_path

        except Exception as e:
            print("Error in initiate_data_transformation:", e)
            raise e