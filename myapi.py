#!/usr/bin/python3

from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12" 
    }
}

@app.get("/")
def index():
    return {"message": "Hello, World!"}
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    if student_id not in students:
        return {"message": "Student not found"}
    else:
        return students[student_id]
