from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Annotated, Optional

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value


def update_patient_data(patient: Patient):

        print(patient.age)
        print(patient.name)
        print(patient.weight)
        print(patient.email)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print('inserted.')
    
patient_info = {'name':'Lucky','age':10,'weight':8, 'email': 'jhalucky61@hdfc.com', 'linkedin_url':'https://linkedin.com/in/theluckyjha', 'married':False, 'allergies':['neurological issues','feats','seizures'],'contact_details':{'Phone no.':'9876543210'}}
    
patient1 = Patient(**patient_info)
    
update_patient_data(patient1)

