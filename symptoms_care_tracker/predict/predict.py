""" import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('illness_prediction_model.pkl')

# Load the dummy columns used during training
dummy_columns = joblib.load('dummy_columns.pkl')

def predict_illness(symptoms):
    # Print received symptoms for debugging
    print("Received Symptoms:\n", symptoms)
    
    # Preprocess input symptoms
    input_data = pd.DataFrame([symptoms])
    print("Input DataFrame:\n", input_data)
    
    # Align input data columns with dummy columns
    input_data = pd.get_dummies(input_data).reindex(columns=dummy_columns, fill_value=0)
    print("Aligned Input Data:\n", input_data)
    
    # Convert input data to numpy array
    input_data_np = input_data.values
    print("Input Data Numpy Array:\n", input_data_np)
    
    # Ensure input_data_np is not empty
    if input_data_np.size == 0:
        raise ValueError("Input data is empty or incorrectly formatted.")
    
    # Make prediction
    prediction = model.predict(input_data_np)
    
    # If prediction is a numpy array, get the first element
    if isinstance(prediction, np.ndarray):
        prediction = prediction[0]
        
    return prediction
 """

import joblib
import pandas as pd
import numpy as np

# Load model and symptom classes
model = joblib.load('illness_prediction_model.pkl')
dummy_columns = joblib.load('dummy_columns.pkl')

def predict_illness(symptoms_dict):
    # Extract active symptoms from the input dictionary
    active_symptoms = [symptom for symptom, present in symptoms_dict.items() if present]
    
    # Initialize a binary array with zeros (matching training structure)
    input_binarized = np.zeros((1, len(dummy_columns)), dtype=int)
    
    # Map active symptoms to their corresponding columns
    for symptom in active_symptoms:
        if symptom in dummy_columns:
            col_index = np.where(dummy_columns == symptom)[0][0]
            input_binarized[0, col_index] = 1
    
    # Make prediction
    prediction = model.predict(input_binarized)
    return prediction[0]