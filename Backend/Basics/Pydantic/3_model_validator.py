from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight: float
    married: bool
    contact: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency(cls, model):
        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model

def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.contact)
    print('Inserted') 
    
    

patient_info = {'name': 'Harsh',
                'age': '59',
                'weight': 75.2,
                'married': False,
                'email': 'abc@hdfc.com',
                'contact': {'phone': '2303834'}}


patient1 = Patient(**patient_info)

insert_patient_info(patient1)
