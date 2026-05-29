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



from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    age:  int
    weight: float
    married: bool
    allergies:  List[str]
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
                'allergies': ['pollen', 'dust'],
                'contact_details': {'email': 'abc@gmail.com', 'phone': '2358769'}}

patient1 = Patient(**patient_info)


insert_patient_info(patient1)
