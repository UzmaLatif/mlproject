import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib_inline
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Lasso,Ridge
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor 
from xgboost import XGBRegressor
import warnings
import os 
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join(os.getcwd(), "artifact", "model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array, test_array,preprocessor_path):
        try:
            print("🔥 Inside Model Trainer")
            logging.info("split training and test input data ")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                "linear regression":LinearRegression(),
                "K-neighbor regressor":KNeighborsRegressor(),
                "Gradient boosting":GradientBoostingRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Random Forest Tree":RandomForestRegressor(),
                "XGBregressor": XGBRegressor(),
                "CatBoostRegressor":CatBoostRegressor(verbose=False),
                "AdaBoostRegressor":AdaBoostRegressor()
            }

            model_report:dict=evaluate_model(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models
            )
             
            #To get the best model score from dictionary
            best_model_score=max(sorted(model_report.values()))

            # to get the best model score from the dictionary
            best_model_name =list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model  =models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found",sys)

            logging.info(f"Best found model on training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            r2_square=r2_score(y_test,predicted)

            return r2_square
    
        except Exception as e:
            raise CustomException(e,sys)






