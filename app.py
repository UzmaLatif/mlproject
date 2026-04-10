from flask import Flask,request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
application =Flask(__name__)
app=application

# Route for the home page
@app.route('/')
def index():
    render_template('index.html')
    @app.route('/predictdata',methods=['GET','POST'])
    def predict_datapoint():
        if request.method =='GET':
            return render_template('home.html')
        else:
            data=CustomData(
                gender=request.form.get('gender'),
                race/ethnicity=request.form.get('race/ethnicity'),
                parental level of education=request.form.get('parental level of education'),
                lunch=request.form.get('lunch'),
                test preparation course.request.form.get('test preparation course')
                reading score=float(request.geet.form('reading score'))
                writing score=float(request.get.form('writing score'))
            )
            pred_df =get_data_as_data_frame()
            print(pred_df)

            predict_pipeline=PreidctPipeline
            results=predict_pipeline.predict(pred_df)
            return render_template('home.html',results=results[0])
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)



