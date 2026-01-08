import requests, random

# URL of your local Flask service
url = 'http://covid-prediction-env.eba-nutu7iqz.us-west-2.elasticbeanstalk.com/predict'

# Example patient data with covid
patient = {
    "age": 45,
    "gender": "male",
    "fever": 1,
    "dry_cough": 1,
    "sore_throat": 0,
    "fatigue": 1,
    "headache": 1,
    "shortness_of_breath": 0,
    "loss_of_smell": 1,
    "loss_of_taste": 0,
    "oxygen_level": 92,
    "body_temperature": 38.5,
    "comorbidity": "diabetes",
    "travel_history": 0,
    "contact_with_patient": 1,
    "chest_pain": 0
}

# Example patient data with no covid
patient_2 = {
    "age": 25,
    "gender": "female",
    "fever": 0,
    "dry_cough": 0,
    "sore_throat": 0,
    "fatigue": 0,
    "headache": 0,
    "shortness_of_breath": 0,
    "loss_of_smell": 0,
    "loss_of_taste": 0,
    "oxygen_level": 98,
    "body_temperature": 36.6,
    "comorbidity": "None",
    "travel_history": 0,
    "contact_with_patient": 0,
    "chest_pain": 0
}

# Select random patient data
random_patient = random.choice([patient, patient_2])

# Send the request and print the response
response = requests.post(url, json=random_patient).json()
print("Patient Data:", random_patient)
print(response)

if response['covid_positive']:
    print("Decision: Patient is likely COVID positive.")
else:
    print("Decision: Patient is likely COVID negative.")