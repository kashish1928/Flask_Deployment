'''import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
#    For rendering results on HTML GUI
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='House price should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)'''
    
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("flask.html")


@app.route("/sampleDG",methods = ['POST'])
def submit():
    if(request.method == "POST"):
        name = request.form["username"]
    return render_template("sampleDG.html", n = name)
        


if __name__ == "__main__":
    app.run(debug=True)