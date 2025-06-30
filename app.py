# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    
    input_df = pd.DataFrame([[location, total_sqft, bath, bhk]],
                            columns=['location', 'total_sqft', 'bath', 'bhk'])
    
    prediction = model.predict(input_df)[0]
    
    return render_template("index.html", prediction_text=f"Predicted price: ₹{prediction:,.2f}")

if __name__ == "__main__":
    app.run(debug=True)