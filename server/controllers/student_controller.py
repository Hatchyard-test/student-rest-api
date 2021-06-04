# controller module
from models.student import Student 


# Get all student from db and return as response model
async def retrieve_students_data():
    pass

# Retrieve a student by id from db and return as response model
async def retrieve_student_data(id):
    pass

# Insert a student into db and return as response model
async def add_student_data(student: Student):
    pass

# Update a student in db and return as response model
async def update_student_data(id,student: Student):
    pass

# Delete a student by id from db
async def delete_student_data(id,user: Student):
    pass


