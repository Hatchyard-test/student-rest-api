from fastapi import FastAPI
from routes.student_bp import student 


app = FastAPI()
app.include_router(student) # Add router blueprints to app
