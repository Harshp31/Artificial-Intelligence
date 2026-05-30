from pydantic import BaseModel

class Adress(BaseModel):
    
    city: str
    state: str
    pin_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    adress: Adress
    
adress_dict = {'city': 'gurgaon', 
               'state': 'Haryana',
               'pin_code': '122001'}

adress1 = Adress(**adress_dict)

patient_dict = {'name': 'Harsh',
                'gender': 'male',
                'age': 35,
                'adress': adress1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.adress.city)
