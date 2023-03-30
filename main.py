from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def get_health():
    return {"Health is OK"}

@app.post("/predict/patient")
async def get_result():
    return {"Positive +"}
