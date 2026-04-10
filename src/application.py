from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# IMPORTANT: import your custom classes
from src.components.pipeline.predict_pipeline import PredictPipeline, CustomData


application = Flask(__name__)
app = application

# Home route
@app.route('/')
def index():
    return render_template('index.html')


# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    
    if request.method == 'GET':
        return render_template('home.html')
    
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),  # FIXED
            parental_level_of_education=request.form.get('parental_level_of_education'),  # FIXED
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),  # FIXED
            reading_score=float(request.form.get('reading_score')),  # FIXED
            writing_score=float(request.form.get('writing_score'))   # FIXED
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)