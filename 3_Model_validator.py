from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')

        return model

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.allergies)
    print(patient.contact_details)


patient_info = {'name':'Lucky','age':'62','weight':8, 'email': 'jhalucky61@hdfc.com', 'linkedin_url':'https://linkedin.com/in/theluckyjha', 'married':False, 'allergies':['neurological issues','feats','seizures'],'contact_details':{'Phone no.':'9876543210', 'emergency':'9090909090'}}
    
patient1 = Patient(**patient_info)
    
update_patient_data(patient1)