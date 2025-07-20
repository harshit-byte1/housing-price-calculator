from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model (no need for preprocessor if it's inside a pipeline)
model = joblib.load('model.pkl')  # Should be a pipeline or include preprocessing

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        feature_names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE',
                         'DIS','RAD','TAX','PTRATIO','B','LSTAT']
        
        input_values = [float(request.form[feature]) for feature in feature_names]
        input_df = pd.DataFrame([input_values], columns=feature_names)

        prediction = model.predict(input_df)[0]

        return render_template('index.html', prediction_text=f"Estimated Price: ${prediction * 1000:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")



if __name__ == "__main__":
    app.run(debug=True)
