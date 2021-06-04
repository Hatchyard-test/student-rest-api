# Blueprint for routes
from fastapi import APIRouter

from controllers.student_controller import (
    retrieve_students_data,
    retrieve_student_data, 
    add_student_data, 
    update_student_data,
    delete_student_data
)

student = APIRouter() 

# Endpoints routes for api
student.get('/', response_description="Students retrieved")(retrieve_students_data)

student.get('/{id}', response_description="Student data retrieved")(retrieve_student_data)

student.post('/', response_description="Student data added into database")(add_student_data)

student.put('/{id}')(update_student_data)

student.delete('/{id}', response_description="Student data deleted from the database")(delete_student_data)

