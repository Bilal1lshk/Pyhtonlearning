from typing import Annotated, Literal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(..., title="Enter the name of the patient")]
    age: Annotated[int, Field(..., title="Enter the age of the patient")]
    city: Literal["Delhi", "Mumbai", "Bangalore"]


# temporary in-memory "database"
patients_db = {}


@app.get("/createdata")
def create_model():
    return {
        "message": "working",
        "status": "perfect"
    }


@app.post("/create_patient")
def create_patient(patient: Patient):
    if patient.id in patients_db:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")

    patients_db[patient.id] = patient.dict()

    return {
        "message": "Patient created successfully",
        "data": patients_db[patient.id]
    }
@app.get("/getingdata")
def allpatient():
    return {"message":patients_db}