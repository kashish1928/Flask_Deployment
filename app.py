#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:59:19 2022

@author: kashishhj
"""


import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('/Users/kashishhj/Desktop/Web Development/bg.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)'''

    return render_template('/Users/kashishhj/Desktop/Web Development/bg.html')

if __name__ == "__main__":
    app.run(debug=True)