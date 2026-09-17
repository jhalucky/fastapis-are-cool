from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

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
    print('inserted.')

patient_info = {'name':'Lucky','age':21}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)


