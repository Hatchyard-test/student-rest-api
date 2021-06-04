# Blueprint for routes
from fastapi import APIRouter
from models.student import StudentResponseModel

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

student.get('/{id}',response_model = StudentResponseModel, response_description="Student data retrieved")(retrieve_student_data)

student.post('/',response_model = StudentResponseModel, status_code=201, response_description="Student data added into database")(add_student_data)

student.put('/{id}',response_model = StudentResponseModel, response_description="Student data update sucessfully")(update_student_data)

student.delete('/{id}', status_code=204, response_description="Student data sucessfully deleted from the database")(delete_student_data)

