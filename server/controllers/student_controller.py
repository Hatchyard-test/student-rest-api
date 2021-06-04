# controller module
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.student import Student,UpdateStudentModel

# import functions of database module
from database.student_db import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student
)

# Get all student from db and return as response model
async def retrieve_students_data():
    students = await retrieve_students()
    return students
    

# Retrieve a student by id from db and return as response model
async def retrieve_student_data(id: str):
    student = await retrieve_student(id)
    if student is None:
        raise HTTPException(status_code=404, detail="Item not found")
    print(student)
    return student


# Insert a student into db and return as response model
async def add_student_data(student: Student):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    print(new_student)
    return new_student

# Update a student in db and return as response model
async def update_student_data(id: str,student: UpdateStudentModel):
    student = jsonable_encoder(student)
    updated_student = await update_student(id, student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_student
   

# Delete a student by id from db
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if not deleted_student:
        raise HTTPException(status_code=404, detail="Item not found")
        


