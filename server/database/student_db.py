from bson.objectid import ObjectId
from config.db import conn

studentDb = conn.student

def student_template(student):
    return {
        "id": str(student["_id"]),
        "firstName": student["firstName"],
        "lastName":student["lastName"],
        "age": student["age"],
        "email": student["email"],
        "course": student["course"],
        "gpa": student["gpa"]
    }

# Add a new student to database
async def add_student(student: dict) -> dict:

    try:
        result = studentDb.insert_one(student)
        newStudent = await  studentDb.find_one({"_id": result.inserted_id})
        return student_template(newStudent)
    except Exception as e:
        print("An exception occurred ::", e)

    

