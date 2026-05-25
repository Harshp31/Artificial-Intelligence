from fastapi import FastAPI

app = FastAPI()     #Creates backend application

@app.get("/")     
def home ():
    return {"message": "FastApi is Working"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get('/about')
def hello():
    return {"message": "Harsh panwar"}