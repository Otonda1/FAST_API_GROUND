#!/usr/bin/python3

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
#datbase simulation as a dict
students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12" 
    }
}
class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def index():
    return {"message": "Hello, World!"}

#path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    if student_id not in students:
        return {"message": "Student not found"}
    else:
        return students[student_id]
    
#query parameters
@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
        
    return {"Data": "Not found"}

#request body
@app.post("/create-student/{student_id}")
def create_studwnt(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]