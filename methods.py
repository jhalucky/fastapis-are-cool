from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('students.json','r') as f:
        data = json.load(f)

        return data


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
def sort_students(sort_by: str = Query(..., description='Sort on the basis of semester'), order: str = Query('asc',desc='sort in asc or desc order')):

    valid_fields = 'semester'

    if sort_by is valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')


    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between in asc and desc')

    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key= lambda x:x.get(sort_by, 0), reverse=sort_order)
