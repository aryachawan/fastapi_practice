from pydantic import BaseModel,EmailStr,field_validator
from typing import List,Dict,Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def valid_age(cls,value):
        if 0 < value < 120:
            return value
        else:
            raise ValueError('Age should be in between 0 and 120')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

patient_info = {'name':'nitish','email':'abc@hdfc.com','age':'30','weight':75.2,'married':True,'contact_details':{'email':'abc@gmail.com','phone':'32244'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)