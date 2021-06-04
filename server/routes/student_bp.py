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

# Error status codes for swagger doc
responses = {
        404: {
            "description": "Error: Not Found",
            "content": {
                "application/json": {
                    "example": {"details": "Item not found"}
                }
            }
        },
        500: {
            "description": "Error: Internal Server Error",
            "content": {
                "application/json": {
                    "example": "Internal Server Error"
                }
            },
        },
}


# Endpoints routes for studentdetails api
student.get('/',responses=responses, response_description="Students retrieved")(retrieve_students_data)

student.get('/{id}',responses=responses,response_model = StudentResponseModel, response_description="Student data retrieved")(retrieve_student_data)

student.post('/', status_code=201,responses=responses,response_model = StudentResponseModel, response_description="Student data added into database")(add_student_data)

student.put('/{id}',responses=responses,response_model = StudentResponseModel, response_description="Student data update sucessfully")(update_student_data)

student.delete('/{id}', status_code=204,responses=responses, response_description="Student data sucessfully deleted from the database")(delete_student_data)

