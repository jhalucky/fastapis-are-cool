from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: Optional[bool] = False
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.weight)
    print(patient.height)
    print('BMI:', patient.calculate_bmi)
    print('updated')


patient_info = {'name':'Lucky','age':'62','weight':8, 'height':1.77, 'email': 'jhalucky61@hdfc.com', 'linkedin_url':'https://linkedin.com/in/theluckyjha', 'married':False, 'allergies':['neurological issues','feats','seizures'],'contact_details':{'Phone no.':'9876543210', 'emergency':'9090909090'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

