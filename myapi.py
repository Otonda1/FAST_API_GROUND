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

#class to handle update requests
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

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

#request body with post
@app.post("/create-student/{student_id}")
def create_studwnt(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

#put request
@app.put("/update-student/{student_id}")
def updatestudent(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

#delete request
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}