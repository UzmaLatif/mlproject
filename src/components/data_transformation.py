import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
      preprocessor_obj_file_path=os.path.join("artifact","preprocessor.pkl")
class DataTransformation:
      def __init__(self):
            self.data_transformation_config=DataTransformationConfig()    
      def get_data_transformer_object(self):
            '''
            This function is responsible for Data transformation
            '''
            try:
                  numerical_columns=["writing score","reading score"]
                  catagorical_columns=[
                        "gender",
                        "race/ethnicity",
                        "parental level of education",         
                        "lunch",
                        "test preparation course"
                  ]
                  # Creating pipelines to numerical and catagorical features
                  num_pipeline= Pipeline(
                      steps=[
                     ("imputer", SimpleImputer (strategy="median")),
                     ("scalar",StandardScaler())

                     ]
                  )
                  cat_pipeline=Pipeline(
                      steps=[
                      ("imputer",SimpleImputer(strategy="most_frequesnt")),
                      ("one_hot_encoder",OneHotEncoder()),
                      ("scalar",StandardScaler())          
                      ]
                  )
                  logging.info("Numerical_columns",numerical_columns)
                  logging.info("Catagorical_columns",catagorical_columns)

                  preprocessor= ColumnTransformer(
                        [
                        ("numerical pieline",num_pipeline,numerical_columns)      
                        ("catagorical pipeline", cat_pipeline,catagorical_columns)
                        ]
                  )
                  return preprocessor
                  
            except Exception as e:
                  raise CustomException(e,sys)   
      def initiate_data_transformation(self,train_path,Test_path): 
            try:
                  train_df=  pd.read_csv(train_path)
                  test_path= pd.read_csv(test_path)
                  logging.info("Read and Test data completed")
                  logging.info("obtaining preprocessing objects")

                  preprocessing_obj=self.get_data_transformer_object()
                  targrt_column_name="math score"

                  numerical_columns=["writing score","reading score"]

                  input_feature_train_df= train_df.drop(columns=[target_column_name],axis=1)
                  target_feature_train_df=train_df[target_column_name]
                   
                  input_feature_test_df= test_df.drop(columns=[target_column_name],axis=1)
                  target_feature_test_df=test_df[target_column_name]

                  logging.info("Applying preprocesssing object on training and testing dataframe")
                   
                  input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df) 
                  input_feature_test_arr=preprocessing_obj.transform(input_feature_train_df)


                  train_arr=np.c_[
                        input_feature_train_arr,np.array(target_feature_train_df)
                  ] 

                  test_arr=np.c_[
                        input_feature_test_arr,np.array[input_feature_test_df]
                  ]
                  logging.info("Saved preprocessing objects.")  
                  
                  save_object(
                        file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocessing_obj
                  )

                  return(
                        train_arr,
                        test_arr,
                        self.data_transformation_config.preprocessor_obj_file_path,
                  )

            except:
                  pass