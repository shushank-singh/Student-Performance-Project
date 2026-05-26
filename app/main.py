import pandas as pd
from fastapi import FastAPI,Depends
import joblib
from schema.model_validation import StudentPerformance,PredictionResponse
from typing import List
import asyncio
from fastapi.middleware.cors import CORSMiddleware

model_lr = joblib.load("model.pkl")

app = FastAPI(title = "Student Mark Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"messege":"Your Student Marks Predictor API Ready !!"}

@app.post("/predict",status_code=201)
async def Predict_Mark(student :List[StudentPerformance]):
    await asyncio.sleep(1)
    data_dict = [s.model_dump() for s in student]
    input_features = pd.DataFrame(data_dict)
    prediction = model_lr.predict(input_features)

    return {
        "status":"Successfull",
        "Total_Records": len(data_dict),
        "Predicted_Mark": prediction.tolist()
    }
