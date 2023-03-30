import joblib
from fastapi import APIRouter
from model.training_model import predict_sepsis


router = APIRouter()

@router.get("/health")
async def get_health():
    return {"Health is OK"}



@router.post("/predict/patient")
async def get_result(patient):
    model = joblib.load("../data/sepsis_model.sav")
    return predict_sepsis(model, patient)
