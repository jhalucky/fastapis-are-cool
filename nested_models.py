from pydantic import BaseModel

from typing import Optional

class Address(BaseModel):

    house_no: str
    street: str 
    city: str
    pincode: int
    state: str
    country: str
    landmark: Optional[str] = None 

class Student(BaseModel):

    name: str
    age: int
    branch: str
    semester: int
    address: Address


address_dict = {'house_no':'142A','street':'Khatana Marg','city':'New Delhi','state':'Delhi','pincode':'110020','country':'India'}

address1 = Address(**address_dict)

student_dict = {'name':'Lucky','age':15,'branch':'B.Tech','semester':7,'address':address1}

student1 = Student(**student_dict)

print(student1)
print(student1.name)
print(student1.address.house_no)