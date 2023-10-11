from flask import Flask,render_template,request
import pandas as pd
import pickle
import numpy as np
app=Flask(__name__)
data=pd.read_csv("Cleaned_Data.csv")
pipe=pickle.load(open('RidgeModel.pkl','rb'))

@app.route("/")
def index():
    locations=sorted(data['location'].unique())
    return render_template("index.html",locations=locations)

@app.route('/predict',methods=['POST'])
def predict():
    locations=request.form.get('location')
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    sqft=request.form.get('total_sqft')
    print(locations,float(bhk),float(bath),float(sqft))
    input=pd.DataFrame([[locations,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=pipe.predict(input)[0]*1e5

    return str(np.round(prediction))
if __name__=="__main__":
    app.run(debug=True,port=5001)