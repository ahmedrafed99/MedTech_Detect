import os

import joblib
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_predict_patient():
    # Load a sample model for testing
    model = joblib.load("model/sepsis_model.sav")

    # Define sample input data
    data = {
        "PRG": 1.2,
        "PL": 3.4,
        "PR": 5.6,
        "SK": 7.8,
        "TS": 9.0,
        "M11": 12.3,
        "BD2": 4.5,
        "Age": 50.0,
    }

    # Send a POST request to the route
    response = client.post("/predict/patient", json=data)

    # Check the response status code
    assert response.status_code == 200

    # Check the response content
    expected_prediction = {"Prediction": 0}  # Replace 0 with the expected prediction value
    assert response.json() == expected_prediction


