# #Dummy for inserting data 
# def insert_patient_data(name: str, age: int):
#     if age < 0:
#         raise ValueError("Age Can't be less than 0")
    
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect Data Type')

# insert_patient_data('Harsh', 21) 


# def update_insert_patient_data(name: str, age: int):
    
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print('Update into database')
#     else:
#         raise TypeError('Incorrect Data Type')

# insert_patient_data('Harsh', 21) 



from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length=50, title='Name Of the Patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'] )]
    email: EmailStr
    linkedIn_url: AnyUrl
    age:  int = Field(gt=0, lt=100)
    weight: Annotated[float, Field(gt=0, Strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the Patient Married or Not')]
    allergies:  Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict [str, str]   
    
    
    
def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')    
    

patient_info = {'name': 'Harsh',
                'age': '30',
                'weight': 75.2,
                'married': False,
                'linkedIn_url': 'http://linkedin.com/1322',
                'allergies': ['pollen', 'dust'],
                'email': 'abc@gmail.com',
                'contact_details': {'phone': '2358769'}}

patient1 = Patient(**patient_info)


insert_patient_info(patient1)