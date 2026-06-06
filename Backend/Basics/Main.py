from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
#HTTPException: It is a special built-in FastAPI used to return custom HTTP error responses when something goes wrong in your API
from pydantic import BaseModel, Field, computed_field
#Path:- Increase the readibility of path parameters
import json
from typing import Annotated, Literal

app = FastAPI()     #Creates backend application

class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description='ID of the patient', example='P001')]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City of the patient')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description='Gender of the Patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in cm')]
    weight: Annotated[float, Field(..., gt=0, description='weight of the patient in kg')]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight) / ((self.height / 100)) ** 2
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= self.bmi < 25:
            return 'Normal weight'
        elif 25 <= self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obesity'       

    

import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "patients.json")


def load_data():
    with open(DATA_PATH, 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)


@app.get("/")     
def start():
    return {'message': 'Patient Management System API'}


@app.get('/about')
def hello():
    return {"message": "A Fully Functional API to manage your patient records"}

@app.get('/view')
def view():
    data = load_data()
    
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    #Load All the patients
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient Not Found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"), order: str = Query('asc', description='sort in asc and desc order')):
    
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse = sort_order)
    
    return sorted_data    
    
    
@app.post('/create')
def create_patient(patient: Patient):
    # load Existing data
    data = load_data()

    # Check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # Add new patient to the data (key by patient.id)
    data[patient.id] = patient.model_dump()

    # Save the updated data back to the file
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created sucessfully'})
    
    

    
    
    