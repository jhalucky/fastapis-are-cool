from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Optional
import json

app = FastAPI()

class Student(BaseModel):
    id: Annotated[str, Field(..., description='ID of the student',examples=['S001'])]
    name: Annotated[str, Field(..., description='Name of the student')]
    age: Annotated[int, Field(..., gt=0, lt=25, description='Age of the student')]
    roll_no: Annotated[int, Field(..., examples=['231000'])]
    course: Annotated[str, Field(...)]
    domain: Annotated[str, Field(...)]
    semester: int
    fees: str

    @computed_field
    @property
    def previous_balances(self) -> int:
        balances = 0
        if self.fees == 'Not paid':
            balances+=10000

        return balances

class StudentUpdate(BaseModel):

    name: Annotated[
        Optional[str],
        Field(description='Name of the student')
    ] = None

    age: Annotated[
        Optional[int],
        Field(gt=0, lt=25, description='Age of the student')
    ] = None

    roll_no: Annotated[
        Optional[int],
        Field(examples=[231000])
    ] = None

    course: Annotated[
        Optional[str],
        Field()
    ] = None

    domain: Annotated[
        Optional[str],
        Field()
    ] = None

    semester: Optional[int] = None

    fees: Optional[str] = None
           

def load_data():
    with open('students.json','r') as f:
        data = json.load(f)

        return data


def save_data(data):
    with open("students.json",'w') as f:
        json.dump(data, f)



@app.get("/")
def hello():
    return {'message': "Student API"}

@app.get("/about")
def about():
    return {'message': 'A functional api.'}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/student/{student_id}")
def view_student(student_id: str = Path(..., description="ID of the student in the db", example='S001')):
    #load the data

    data = load_data()

    if student_id in data:
        return data[student_id]

    raise HTTPException(status_code=404, detail='patient not found')


@app.get('/sort')
def sort_students(sort_by: str = Query(..., description='Sort on the basis of semester'), order: str = Query('asc',description='sort in asc or desc order')):

    valid_fields = ['semester','age']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')


    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between in asc and desc')

    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key= lambda x:x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


@app.post('/register-student')
def create_student(student: Student):

    # load existing data
    data = load_data()

    # check if student already exists
    if student.id in data:
        raise HTTPException(status_code=400,detail='Student already exists')

    # new student to the db
    data[student.id] = student.model_dump(exclude=['id'])

    # save 
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patient created successfully'})

@app.put('/edit/{student_id}')
def update_student(student_id: str, student_update: StudentUpdate):

    data = load_data()

    if student_id not in data:
        raise HTTPException(status_code=400, detail='Student not found')

    existing_student_info = data[student_id]

    updated_student_info = student_update.model_dump(exclude_unset=True)

    for key, value in updated_student_info.items():
        existing_student_info[key] = value

    existing_student_info['id'] = student_id
    pydantic_student_obj = Student(**existing_student_info)

    existing_student_info = pydantic_student_obj.model_dump(exclude='id')

    data[student_id] = existing_student_info 


    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient updated" })


@app.delete('/delete/{student_id}')
def  delete_student(stduent_id: str):

    data = load_data()

    if stduent_id not in data:
        raise HTTPException(status_code=404, detail='Student not found')

    del data[stduent_id]

    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Student deleted."})