Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import flask
from flask.app import Flask

from flask import Flask, render_template,request
import pandas as pd
import joblib

model = joblib.load('pipe.pkl')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/predict",methods = ['POST'])
def predict():
    test_pd = pd.DataFrame([request.form])
    value = model.predict(test_pd)[0]
    #return request.form
    value = str(round(value,2))
    return render_template("predict.html",price = value +" Lakhs")

if __name__ == '__main__':
    app.run(debug=True)