from fastapi import FastAPI
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