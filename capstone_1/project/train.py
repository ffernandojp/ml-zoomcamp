import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

# 1. Data Loading and Preparation
print("Loading and preparing data...")
df = pd.read_csv('covid19_patient_symptoms_diagnosis.csv')

# Standardize column names (from EDA step)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Data Cleaning: Handle missing comorbidities identified in EDA
df['comorbidity'] = df['comorbidity'].fillna('none')

# Define features and target
y = df.covid_result.values
# Dropping patient_id as it's an identifier, not a predictor
df_train = df.drop(columns=['covid_result', 'patient_id'])

# Define feature sets
categorical = ['gender', 'comorbidity']
numerical = ['age', 'oxygen_level', 'body_temperature']
binary_symptoms = [
    'fever', 'dry_cough', 'sore_throat', 'fatigue', 'headache',
    'shortness_of_breath', 'loss_of_smell', 'loss_of_taste',
    'chest_pain', 'travel_history', 'contact_with_patient'
]
features = categorical + numerical + binary_symptoms

# 2. Vectorization (Preprocessing)
print("Preprocessing features...")
train_dicts = df_train[features].to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)

# 3. Training the Final Model
# Using the best parameters found during the tuning step in the notebook
print("Training the final model (Random Forest, depth=10)...")
final_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=1,
    n_jobs=-1
)
final_model.fit(X_train, y)

# 4. Exporting the Model (Pickle)
output_file = 'model.bin'
print(f"Saving the model to {output_file}...")

with open(output_file, 'wb') as f_out:
    # Save both the DictVectorizer and the model to ensure consistent preprocessing
    pickle.dump((dv, final_model), f_out)

print("Training script completed successfully.")