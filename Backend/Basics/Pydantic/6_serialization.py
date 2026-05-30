from pydantic import BaseModel


class Adress(BaseModel):
    
    city: str
    state: str
    pin_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str = 'Male'
    adress: Adress
    
    
adress_dict = {'city': 'gurgaon', 
               'state': 'Haryana',
               'pin_code': '122001'}

adress1 = Adress(**adress_dict)

patient_dict = {'name': 'Harsh',
                'age': 35,
                'gender': 'Male',
                'adress': adress1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude = {'adress':['state']}) #include and exclude methods #Exclude_unset also
temp1 = patient1.model_dump_json()
print(temp)
print(type(temp))
