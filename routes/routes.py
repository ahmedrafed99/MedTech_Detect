import os

import joblib
from fastapi import APIRouter, Request
from model.training_model import predict_sepsis
from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/health")
async def get_health():
    return {"Health is OK"}


#
# @router.post("/predict/patient")
# async def get_result(patient):
#     model = joblib.load("../model/sepsis_model.sav")
#     return predict_sepsis(model, patient)

@router.post("/predict/patient")
async def get_result(PRG: float = Form(...), PL: float = Form(...), PR: float = Form(...), 
                     SK: float = Form(...), TS: float = Form(...), M11: float = Form(...), 
                     BD2: float = Form(...), Age: float = Form(...)):
    patient = {"PRG": PRG, "PL": PL, "PR": PR, "SK": SK, "TS": TS, "M11": M11, "BD2": BD2, "Age": Age}
    print(patient)
    model = joblib.load("model/sepsis_model.sav")

    prediction = predict_sepsis(model, patient)
    return {"Prediction": int(prediction)}  

