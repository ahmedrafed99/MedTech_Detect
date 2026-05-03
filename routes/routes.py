import os
import joblib
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model.training_model import predict_sepsis

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    """
    Render the home page.

    Parameters:
        request (Request): The incoming request object.

    Returns:
        TemplateResponse: The rendered home page HTML template.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/health")
async def get_health():
    """
    Check the health status of the API.

    Returns:
        dict: A JSON response indicating the health status.
    """
    return {"Health is OK"}

@router.post("/predict/patient")
async def get_result(PRG: float = Form(...), PL: float = Form(...), PR: float = Form(...),
                     SK: float = Form(...), TS: float = Form(...), M11: float = Form(...),
                     BD2: float = Form(...), Age: float = Form(...)):
    """
    Predict sepsis for a given patient based on the provided parameters.

    Parameters:
        PRG (float): The value of PRG parameter.
        PL (float): The value of PL parameter.
        PR (float): The value of PR parameter.
        SK (float): The value of SK parameter.
        TS (float): The value of TS parameter.
        M11 (float): The value of M11 parameter.
        BD2 (float): The value of BD2 parameter.
        Age (float): The value of Age parameter.

    Returns:
        dict: A JSON response containing the sepsis prediction.
    """
    patient = {"PRG": PRG, "PL": PL, "PR": PR, "SK": SK, "TS": TS, "M11": M11, "BD2": BD2, "Age": Age}
    print(patient)
    model = joblib.load("model/sepsis_model.sav")

    prediction = predict_sepsis(model, patient)
    return {"Prediction": int(prediction)}
