from models.student import Student,UpdateStudentModel, StudentResponseModel
import json

# Test student model
def test_new_student():
    student = Student(
        firstName =  "Lasitha",
        lastName = "Jayawardana",
        age = 20,
        email =  "user@example.com",
        course = "engineering",
        gpa =  4)
    
    assert student.firstName == 'Lasitha'
    assert student.lastName == 'Jayawardana'
    assert student.age == 20
    assert student.email == 'user@example.com'
    assert student.course == 'engineering'
    assert student.gpa == 4
    

# Test UpdateStudentModel
def test_new_UpdateStudentModel():
    student = UpdateStudentModel(
        firstName =  "Lasitha",
        lastName = "Jayawardana",
        age = 20,
        email =  "user@example.com",
        course = "engineering",
        gpa =  4)
    
    assert student.firstName == 'Lasitha'
    assert student.lastName == 'Jayawardana'
    assert student.age == 20
    assert student.email == 'user@example.com'
    assert student.course == 'engineering'
    assert student.gpa == 4
        
    
# Test StudentResponseModel
def test_new_StudentResponseModel():
    student = StudentResponseModel(
        id = "emnffjefjnefwjnefefnwfjn",
        firstName =  "Lasitha",
        lastName = "Jayawardana",
        age = 20,
        email =  "user@example.com",
        course = "engineering",
        gpa =  4)

    assert student.id == 'emnffjefjnefwjnefefnwfjn'
    assert student.firstName == 'Lasitha'
    assert student.lastName == 'Jayawardana'
    assert student.age == 20
    assert student.email == 'user@example.com'
    assert student.course == 'engineering'
    assert student.gpa == 4