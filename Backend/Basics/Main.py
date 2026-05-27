from fastapi import FastAPI, Path, HTTPException
#HTTPException: It is a special built-in FastAPI used to return custom HTTP error responses when something goes wrong in your API

#Path:- Increase the readibility of path parameters
import json

app = FastAPI()     #Creates backend application

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

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


    