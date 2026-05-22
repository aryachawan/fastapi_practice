from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
         if model.age > 60 and 'emergency' not in model.contact_details:
             raise ValueError('Patients older than 60 must have an emergency contact no')
         return model


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('inserted')

patient_info = {'name':'nitish','email':'abc@hdfc.com','age':'65','weight':75.2,'married':True,'contact_details':{'phone':'32244','emergency':'23443'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)