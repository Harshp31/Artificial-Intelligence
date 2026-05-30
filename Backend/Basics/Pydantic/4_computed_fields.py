from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float #kg
    height: float #m
    married: bool

    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/self.height**2,2)
        return bmi
    

def update_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print('BMI', patient.calculate_bmi)
    print(patient.married)
    print('Inserted') 
    
    
    
patient_info = {'name': 'Harsh',
                'age': 23,
                'email': 'abc@hdfc.com',
                'weight': 88.2,
                'height': 1.83,
                'married': False}

patient1 = Patient(**patient_info)

update_patient_info(patient1)
    
