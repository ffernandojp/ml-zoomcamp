# 🍷 Red Wine Quality Prediction Project

## 1. Description of the Problem

The goal of this project is to develop a machine learning model capable of predicting the quality class of red wine based solely on its measurable physiochemical properties.

### Problem Framing

We approach this as a binary classification problem, similar to the Churn Prediction project. Wine samples are categorized as either **"Bad Quality"** or **"Good Quality"**:

- **Good Quality (Target = 1):** Wine samples with a quality score of 7 or higher.
- **Bad Quality (Target = 0):** Wine samples with a quality score of 6 or lower.

### How the Solution Will Be Used

This model provides a fast, non-destructive, and low-cost screening tool for the wine industry. Instead of relying solely on expensive and time-consuming manual sensory evaluations by expert tasters, wineries can run standard chemical tests on a batch (e.g., measuring fixed acidity, volatile acidity, chlorides, and sulfur dioxide) and feed these values into the web service. The model provides an immediate, probabilistic prediction of whether the batch is likely to achieve a high-quality rating, allowing quality control teams to prioritize which batches require immediate attention or further costly analysis.

### Evaluation Metric

Due to the likely imbalance in the target variable (often fewer wines achieve "Good Quality"), the primary evaluation metric for model selection will be the **Area Under the ROC Curve (AUC-ROC)**, as discussed in the Classification Evaluation Metrics materials.

---

## 2. Instructions on How to Run the Project (Reproducibility & Deployment)

This section ensures that the project meets reproducibility criteria, dependency management, and containerization requirements. The project requires Python 3.9+, with git and Docker installed.

### A. Setting up the Environment and Dependencies

Follow these steps to correctly set up and manage project dependencies:

1. **Clone the Repository:**
```bash
git clone <repository_url>
cd <repository_folder>/midterm_project
```
2. **Install Dependencies:**  
The project uses `requirements.txt` to manage dependencies, including libraries such as `pandas`, `scikit-learn`, and `Flask`.
```bash
python -m venv env
source env/bin/activate # On Windows use env\Scripts\activate
pip install -r requirements.txt
```
### B. Training the Model (`train.py`)

This script encapsulates the final training logic from the notebook, retraining the chosen model and saving it for deployment.

1. Run the training script:
```bash
python train.py
```
- **Output:** This script trains the model and saves the resulting model artifact (e.g., using pickle) as `model.bin`.

### C. Running the Web Service Locally (`predict.py`)

The `predict.py` script loads the saved model and exposes a web service using Flask framework.

1. Start the prediction service:
```bash
python predict.py
```
- The service will run locally and is typically accessible at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **API Usage Example (POST /predict):**  
The endpoint accepts a JSON array of wine attributes and returns a prediction probability and class.

3. **Example Request (curl):**
This example shows how to send a POST request with two wine samples to the local web service, where one is high quality and the other is low quality.
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '[
  {
    "fixed_acidity": 7.0,
    "volatile_acidity": 0.20,
    "citric_acid": 0.35,
    "residual_sugar": 2.0,
    "chlorides": 0.050,
    "free_sulfur_dioxide": 15.0,
    "total_sulfur_dioxide": 40.0,
    "density": 0.9950,
    "ph": 3.40,
    "sulphates": 0.85,
    "alcohol": 13.0
  },
  {
    "fixed_acidity": 8.5,
    "volatile_acidity": 0.80,
    "citric_acid": 0.10,
    "residual_sugar": 3.5,
    "chlorides": 0.110,
    "free_sulfur_dioxide": 30.0,
    "total_sulfur_dioxide": 100.0,
    "density": 0.9985,
    "ph": 3.60,
    "sulphates": 0.45,
    "alcohol": 9.0
  }
]'
```
4. **Example Response:**
```json
[
  {
    "probability_of_good_quality": 0.7035,
    "wine_quality_prediction": 1
  },
  {
    "probability_of_good_quality": 0.001,
    "wine_quality_prediction": 0
  }
]
```
### D. Containerization with Docker

The application is containerized, and the following instructions describe how to build and run the container.

1. **Build the Docker Image:**  
Ensure there is a `Dockerfile` in the root directory.
```bash
docker build -t red-wine-quality .
```
2. **Run the Docker Container:**
```bash
docker run -p 5000:5000 red-wine-quality
```
- This maps the container's port `5000` to the local port `5000`. The service will then be accessible via: [http://localhost:5000/predict](http://localhost:5000/predict).

---