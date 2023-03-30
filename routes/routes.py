from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def get_health():
    return {"Health is OK"}

@router.post("/predict/patient")
async def get_result():
    return {"Positive +"}
