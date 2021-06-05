from fastapi.testclient import TestClient 
from main import app 

client = TestClient(app)

objId = ""

# Input data for test
inputData ={
  "firstName": "Lasitha",
  "lastName": "Jayawardana",
  "age": 20,
  "email": "user@example.com",
  "course": "engineering",
  "gpa": 4
}

# Input data for update for test
updateData = {
  "firstName": "Nimal",
  "lastName": "Jayawardana",
  "course": "engineering",
  "gpa": 4
}

# Input invalid data for test
invalidData ={
  "firstName": "Lasitha",
  "lastName": "Jayawardana",
  "age": 20,
  "email": "user@example.com",
  "course": "engineering",
  "gpa": 55
}

# Expected Response data for test as function
def outputData(id):
  return {
      "id": id,
      "firstName": "Lasitha",
      "lastName": "Jayawardana",
      "age": 20,
      "email": "user@example.com",
      "course": "engineering",
      "gpa": 4.0
  }

# Test Insert a student into db api endpoint 
def test_add_student_data():
    response = client.post("/api/", json=inputData)
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    response_body = response.json()
    global objId
    objId = response_body["id"]
    assert len(objId) == 24

# Test Insert a student into db api endpoint with validation error
def test_add_student_data_invalid():
    response = client.post("/api/", json=invalidData)
    assert response.status_code == 422


# Test get all student from db api endpoint 
def test_retrieve_students_data():
    response = client.get("/api/")
    assert response.status_code == 200
    output = outputData(objId)
    assert output in response.json()


# Test retrieve a student by id from db api endpoint 
def test_retrieve_student_data():
    response = client.get("/api/" + objId + "")
    assert response.status_code == 200
    output = outputData(objId)
    assert output == response.json()

# Test retrieve a student by id from db api endpoint with wrone id
def test_retrieve_student_data_404():
    response = client.get("/api/someid")
    assert response.status_code == 404


# Test Update a student in db api endpoint 
def test_update_student_data():
    response = client.put("/api/" + objId + "", json=updateData)
    assert response.status_code == 200

# Test Update a student in db api endpoint with wrone id
def test_update_student_data_404():
    response = client.put("/api/someid", json=updateData)
    assert response.status_code == 404


# Test Delete a student by id api endpoint 
def test_delete_student_data():
    response = client.delete("/api/" + objId + "")
    assert response.status_code == 204

# Test Delete a student by id api endpoint with wrone id
def test_delete_student_data_404():
    response = client.delete("/api/someid")
    assert response.status_code == 404
