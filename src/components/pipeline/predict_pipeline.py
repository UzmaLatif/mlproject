'''import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            #model_path = r'artifact\model.pkl'
            model_path = r'D:\mlproject\artifact\model.pkl'
            preprocessor_path = r'D:\mlproject\artifact\preprocessor.pkl'
            
           #preprocessor_path = r'artifact\preprocessor.pkl'
           
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)

def get_data_as_data_frame(self):
    try:
        custom_input_data_dict = {
            "gender": [self.gender],
            "race/ethnicity": [self.race_ethnicity],
            "parental level of education": [self.parental_level_of_education],
            "test preparation course": [self.test_preparation_course],
            "lunch": [self.lunch],
            "reading score": [self.reading_score],
            "writing score": [self.writing_score]
        }
        return pd.DataFrame(custom_input_data_dict)
    except Exception as e:
        raise CustomException(e, sys)
def get_data_as_data_frame(self):
    try:
        custom_input_data_dict = {
            "gender": [self.gender],
            "race/ethnicity": [self.race_ethnicity],
            "parental level of education": [self.parental_level_of_education],
            "test preparation course": [self.test_preparation_course],
            "lunch": [self.lunch],
            "reading score": [self.reading_score],
            "writing score": [self.writing_score]
        }
        return pd.DataFrame(custom_input_data_dict)
    except Exception as e:
        raise CustomException(e, sys)    
    



    def get_data_as_data_frame(self):
        try:
            custom_input_data_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "test_preparation_course": [self.test_preparation_course],
                "lunch": [self.lunch],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(custom_input_data_dict)
        except Exception as e:
            raise CustomException(e, sys)'''
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Paths (safe raw strings)
            model_path = r"D:\mlproject\artifact\model.pkl"
            preprocessor_path = r"D:\mlproject\artifact\preprocessor.pkl"

            # Load objects
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Transform input data
            data_scaled = preprocessor.transform(features)

            # Predict
            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 test_preparation_course: str,
                 lunch: str,
                 reading_score: int,
                 writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.test_preparation_course = test_preparation_course
        self.lunch = lunch
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            data_dict = {
                # IMPORTANT: must match training column names EXACTLY
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "test preparation course": [self.test_preparation_course],
                "lunch": [self.lunch],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score]
            }

            return pd.DataFrame(data_dict)

        except Exception as e:
            raise CustomException(e, sys)