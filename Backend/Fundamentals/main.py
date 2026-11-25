#Import the fastapi class from the FastAPI Package 
from fastapi import FastAPI

#Create an FastAPI application 
app = FastAPI(title="Backend API")

#First API Endpoint 
@app.get("/")
def home():
    return {"message": "Welcome"}

#Second API Endpoint
@app.get("/health")
def health_check():
    return {"Status": "Healthy"}

#Third API Endpoint
@app.get("/about")
def about():
    return {
        "application": "Backend API",
        "framework" : "FastAPI",
        "version": "1.0"
    }

#Fourth API Endpoint
@app.get("/contact")
def contact():
    return {
        "Phone no.": "7248xxxxx"
    }

    