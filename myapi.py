#!/usr/bin/python3

from fastapi import FastAPI

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
def get_student(student_id: int):
    if student_id not in students:
        return {"message": "Student not found"}
    else:
        return students[student_id]
