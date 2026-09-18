from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=100, title='Name of the Patient')]
    age: int = Field(gt=0, lt=120, strict=True)
    weight: float = Field(gt=0, strict=True)
    email: EmailStr
    linkedin_url: AnyUrl
    married: Optional[bool] = True
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


# def insert_patient_data(name, age):

#     if type(name) == str and type(age) == int:
        
#         print(name)
#         print(age)
#         print('Data inserted into db.')

#     else:
#         raise TypeError('Incorrect datatype.')



# insert_patient_data('nitish', 21)

# def update_patient_data(name: str, age: int):

#     if type(name) == str and type(age) == int:
        
#         print(name)
#         print(age)
#         print('Data updated.')

#     else:
#         raise TypeError('Incorrect datatype.')

# update_patient_data('nitish', 31)

def insert_patient_data(patient: Patient):

    print(patient.age)
    print(patient.name)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted.')

patient_info = {'name':'Lucky','age':10,'weight':8, 'email': 'jhalucky61@gmail.com', 'linkedin_url':'https://linkedin.com/in/theluckyjha', 'married':False, 'allergies':['neurological issues','feats','seizures'],'contact_details':{'Phone no.':'9876543210'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)


