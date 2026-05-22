from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print(patient.allergies)
    print('inserted')

patient_info = {'name':'nitish','email':'abc@hdfc.com','age':'65','weight':75.2,'height':1.72,'married':True,'contact_details':{'phone':'32244','emergency':'23443'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)
print(type(patient1))
temp = patient1.model_dump()
print(type(temp))
temp1 = patient1.model_dump_json()
print(type(temp1))