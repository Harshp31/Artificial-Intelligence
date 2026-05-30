from pydantic import BaseModel, EmailStr, AnyUrl, field_validator, ValidationError
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    contact: Dict[str, str]

    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value:str):
        
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a Valid domain')
        
        return value   
    
    @field_validator('name')
    @classmethod
    def name_validator(cla, value: str):
        return value.upper()     
    
    @field_validator('age', mode='after') #There are two modes before and after of type coercion
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age SHould be in between 1 and 100')    
    
def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.contact)
    print('Inserted')    
    

patient_info = {'name': 'Harsh',
                'age': '30',
                'weight': 75.2,
                'married': False,
                'email': 'abc@hdfc.com',
                'contact': {'phone': '2303834'}}

patient1 = Patient(**patient_info)

insert_patient_info(patient1)
