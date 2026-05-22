from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str,Field(...,description='ID of the patient',examples=['P001','P004'])]
    name: Annotated[str,Field(...,description='Name of the patient')]
    city: Annotated[str,Field(...,description='City where the patient is living')]
    age: Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender: Annotated[Literal['Male','Female','Other'],Field(...,description='Gender of the patient')]
    height: Annotated[float,Field(...,gt=0,description='Height of the patient in meters')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the patient in kg')]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if(self.bmi<18.5):
            return 'Underweight'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str],Field(default=None)]
    city: Annotated[Optional[str],Field(default=None)]
    age: Annotated[Optional[int],Field(default=None,gt=0,lt=120)]
    gender: Annotated[Optional[Literal['Male','Female','Other']],Field(default=None)]
    height: Annotated[Optional[float],Field(default=None,gt=0)]
    weight: Annotated[Optional[float],Field(default=None,gt=0)]


#helper functions
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")
def about():
    return {'message':'Functional API to manage your patient records'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,description='ID of the patient',examples='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404,detail='Patient not found')

@app.get('/sort')
def sort_patient(sort_by: str = Query(...,description='Sort data by height,weight or bmi'),order : str = Query('asc',description='sort data in asecnding or descending order')):
    data = load_data()
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Inavlid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Inavlid order select between ascending and descending')
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')
    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'Patient created successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    