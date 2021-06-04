# controller module
from fastapi.encoders import jsonable_encoder
from models.student import Student, ErrorResponseModel, ResponseModel,UpdateStudentModel

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
    if students:
        return ResponseModel(students, "Students data retrieved successfully")
    return ResponseModel(students, "Empty list returned")



# Retrieve a student by id from db and return as response model
async def retrieve_student_data(id: str):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

# Insert a student into db and return as response model
async def add_student_data(student: Student):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    print(new_student)
    return ResponseModel(new_student, "Student added successfully")

# Update a student in db and return as response model
async def update_student_data(id: str,student: UpdateStudentModel):
    pass

# Delete a student by id from db
async def delete_student_data(id: str):
    pass


