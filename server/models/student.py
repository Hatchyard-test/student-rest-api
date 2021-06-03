from pydantic import BaseModel

class Student(BaseModel):
    studentId:str
    firstName: str
    lastName:str
    age: int
    email: str
    