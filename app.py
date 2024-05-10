from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open(f'model2.pkl', "rb"))

app = Flask(__name__)

features = ['HubTemperature', 'MainBoxTemperature', 'WindDirection',
       'NacellePosition', 'AmbientTemperatue', 'TurbineStatus', 'WindSpeed']
print(features)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['GET','POST'])

def predict():
    
    d = {'HubTemperature':float(request.form.get('HubTemperature')), 
        'MainBoxTemperature':float(request.form.get('MainBoxTemperature')), 
        'WindDirection':float(request.form.get('WindDirection')),
        'NacellePosition':float(request.form.get('NacellePosition')), 
        'AmbientTemperatue':float(request.form.get('AmbientTemperatue')), 
        'TurbineStatus':float(request.form.get('TurbineStatus')), 
        'WindSpeed':float(request.form.get('WindSpeed'))}
    df = pd.DataFrame([d])
    return render_template('index.html', prediction_text = model.predict(df))

if __name__ == "__main__":
    app.run(debug=True)