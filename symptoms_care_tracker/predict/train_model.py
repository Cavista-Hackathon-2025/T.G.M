""" import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Loading dataset
data = pd.read_csv('myenv/symptoms_care_tracker/predict/dataset.csv')

# Processing data
symptom_columns = ['Symptom_1','Symptom_2','Symptom_3','Symptom_4','Symptom_5','Symptom_6','Symptom_7','Symptom_8','Symptom_9','Symptom_10','Symptom_11','Symptom_12','Symptom_13','Symptom_14','Symptom_15','Symptom_16','Symptom_17']
x = data[symptom_columns]

# Filling columns of x that doesnt have a value 
x = x.fillna(0)

y = data['Disease']

x = pd.get_dummies(x)

# Save dummy columns to a file
joblib.dump(x.columns, 'dummy_columns.pkl')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# Save model
joblib.dump(model, 'illness_prediction_model.pkl')

 """

import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv('myenv/symptoms_care_tracker/predict/dataset.csv')
symptom_columns = [f'Symptom_{i}' for i in range(1, 18)]  # Adjust based on your columns

# Extract all symptoms per row (ignore NaNs/0)
data['symptoms'] = data[symptom_columns].apply(
    lambda row: [s for s in row if pd.notna(s) and s != 0], axis=1
)

# Binarize symptoms (creates one column per unique symptom)
mlb = MultiLabelBinarizer()
x = mlb.fit_transform(data['symptoms'])
x = pd.DataFrame(x, columns=mlb.classes_)

# Save the binarizer's classes for prediction
joblib.dump(mlb.classes_, 'dummy_columns.pkl')

# Train model
y = data['Disease']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)
joblib.dump(model, 'illness_prediction_model.pkl')