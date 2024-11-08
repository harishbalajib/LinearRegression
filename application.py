import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application=Flask(__name__)
app=application

#import ridge regressor and StandardScaler pickle file
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('/Users/harish/Documents/Python/Machine Learning/Practice/models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/PredictData",methods=['GET','POST' ])
def predict_datapoint():
    if request.method=="POST":
       
        temperature = float(request.form.get('Temperature'))
        rh = float(request.form.get('RH'))
        ws = float(request.form.get('Ws'))
        rain = float(request.form.get('Rain'))
        ffmc = float(request.form.get('FFMC'))
        dmc = float(request.form.get('DMC'))
        isi = float(request.form.get('ISI'))
        classes = request.form.get('Classes')
        region = request.form.get('Region')

        # Combine all extracted values into a dictionary for processing or prediction
        new_data_Scaled=standard_scaler.transform([[temperature,rh,ws,rain,ffmc,dmc,isi,classes,region]])
        result=ridge_model.predict(new_data_Scaled)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")