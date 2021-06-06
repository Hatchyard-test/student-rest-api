from pydantic import BaseModel, EmailStr, Field
from typing import Optional

#Student base model class
class Student(BaseModel):
    firstName: str= Field(...)
    lastName:str= Field(...)
    age:  int = Field(...)
    email: EmailStr = Field(...)
    course:str = Field(...)
    gpa: float = Field(..., le=4.0)

    class Config:
        schemaExtra = {
            "example": {
                "firstName": "Lasitha",
                "lastName": "Jayawardana",
                "age": 26,
                "email": "lasitha@gmail.com",
                "course": "Engineering",
                "gpa": "3.2"
            }
        }

#Student model class for update
class UpdateStudentModel(BaseModel):
    firstName: Optional[str]
    lastName :Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]
    course: Optional[str]
    gpa: Optional[float]

    class Config:
        schemaExtra = {
            "example": {
                "firstName": "Lasitha",
                "lastName": "Jayawardana",
                "age": 26,
                "email": "lasitha@gmail.com",
                "course": "Science",
                "gpa": "3.8"
            }
        }

# Api response model
class StudentResponseModel(BaseModel):
    id: str= Field(...)
    firstName: str= Field(...)
    lastName:str= Field(...)
    age:  int = Field(...)
    email: EmailStr = Field(...)
    course:str = Field(...)
    gpa: float = Field(..., le=4.0)



# #Return structure as response when suceed
# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }

# #Return structure as response when error
# def ErrorResponseModel(error, code, message):
#     return {
#         "error": error,
#         "code": code,
#         "message": message,
#     }