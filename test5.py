from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict={'city':'Mumbai','state':'maharashatra','pincode':'400043'}
address1=Address(**address_dict)
patient_dict={'name':'Arya','gender':'Male','age':12,'address':address1}
patient1=Patient(**patient_dict)
print(patient1)
print(patient1.address.city)