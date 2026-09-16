from fastapi import FastAPI, Path, HTTPException
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
