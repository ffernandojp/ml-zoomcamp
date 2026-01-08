import pickle
from flask import Flask, request, jsonify

# 1. Load the saved DictVectorizer and Model 
model_file = 'model.bin'
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# 2. Initialize the Flask application 
app = Flask('covid-prediction')

# 3. Define the prediction endpoint 
@app.route('/predict', methods=['POST'])
def predict():
    # Get patient data from the request (JSON format)
    patient = request.get_json()

    # Preprocess the input using the loaded DictVectorizer
    X = dv.transform([patient])

    # Get the probability of being COVID positive
    y_pred = model.predict_proba(X)[0][1]
    covid_positive = y_pred >= 0.5

    # Prepare the JSON response
    result = {
        'covid_probability': float(y_pred),
        'covid_positive': bool(covid_positive)
    }

    return jsonify(result)

# 4. Run the service (locally for testing)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)