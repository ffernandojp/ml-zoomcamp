# 🦠 COVID-19 Patient Diagnosis Prediction Project

## 1. Description of the Problem

The goal of this project is to develop a machine learning model capable of predicting the likelihood of a patient testing positive for COVID-19 based on their symptoms, vital signs (oxygen levels and temperature), and clinical history.

### Problem Framing
We approach this as a binary classification problem. The model predicts whether a patient is likely to be:
- COVID Positive (Target = 1)
- COVID Negative (Target = 0)

### How the Solution Will Be Used
This service acts as a preliminary screening and triage tool. Medical staff or individuals can input symptoms (such as fever, cough, or loss of taste) and vital signs into the web service. The model provides an immediate probability score, allowing healthcare providers to prioritize patients for official PCR testing or immediate isolation in resource-constrained environments.

### Evaluation Metric
Given that health datasets can be imbalanced, the primary evaluation metric for this model is the Area Under the ROC Curve (AUC-ROC). This ensures the model effectively distinguishes between positive and negative cases regardless of the class distribution.

------------------------------------------------------------------

## 2. Instructions on How to Run the Project

This project requires Python 3.9+, Pipenv or Virtualenv, and Docker.

### A. Setting up the Environment and Dependencies

To manage dependencies and ensure reproducibility, this project uses a virtual environment:

1. **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd covid-prediction-project
    ```
2. **Install Dependencies:**
    ```bash
    pipenv install --dev  # or pipenv install for production
    pipenv shell
    ```



### B. Training the Model (train.py)

The train.py script performs the final data cleaning, trains the tuned model, and saves the logic as a binary file.

1. **Run the training script:**
    ```bash
    python train.py
    ```
**Output:** Generates model.bin containing the DictVectorizer and the trained model.

### C. Running the Web Service Locally (predict.py)
The service uses Flask and Gunicorn to serve predictions.
1. **Start the service:**

    ```bash    
    gunicorn --bind 0.0.0.0:5000 predict:app
    ```
2. **Example Request (using Python):**

    ```python
        import requests

        url = "http://localhost:5000/predict"
        patient_data = {
            "symptoms": "fever,cough,loss_of_taste",
            "oxygen_level": 92,
            "temperature": 38.5
        }
        response = requests.post(url, json=patient_data)
        print(response.json())
    ```
### D. Containerization with Docker

The application is fully containerized to ensure it runs in any environment.

1. **Build the Image:**

    ```bash
    docker build -t covid-predictor .
    ```

2. **Run the Container:**

    ```bash
    docker run -p 5000:5000 covid-predictor
    ```

### E. Cloud Deployment (AWS Elastic Beanstalk)

This project is deployed to the cloud using AWS Elastic Beanstalk for high availability.

**Deployment Steps:**

1. **Initialize EB:**
    ```bash
    eb init -p docker covid-prediction-project
    ```



2. **Create Environment:**

    ```bash
    eb create covid-prediction-env
    ```

3. **Live URL:** The service is available for testing at: http://covid-prediction-env.eba-nutu7iqz.us-west-2.elasticbeanstalk.com/predict

**Testing the Cloud Service:**

To test the live model, update your test script url to the Beanstalk address provided above. You can send a POST request to the Beanstalk URL with patient data in JSON format. Below are two examples: one for a patient likely to test positive and one for a patient likely to test negative.

**Example 1: Positive**
```json
    {
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
```
**Output:**
![COVID Positive Example#311px #144px](project/images/covid-positive-patient.png)


**Example 2: Negative**
```json
    {
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
```
**Output:**
![COVID Negative Example](project/images/covid-negative-patient.png)


**Teardown:**

To avoid unnecessary AWS costs, terminate the environment after review:

```bash
    eb terminate covid-prediction-env
```