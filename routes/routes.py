import os

import joblib
from fastapi import APIRouter
from model.training_model import predict_sepsis
from fastapi import Form
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/health")
async def get_health():
    return {"Health is OK"}


#
# @router.post("/predict/patient")
# async def get_result(patient):
#     model = joblib.load("../model/sepsis_model.sav")
#     return predict_sepsis(model, patient)

@router.post("/predict/patient", response_class=HTMLResponse)
async def get_result(patient: dict = Form(...)):
    print(os.O_PATH)
    model = joblib.load("model/sepsis_model.sav")

    prediction = predict_sepsis(model, patient)
    return f"<h1>Prediction: {prediction}</h1>"
