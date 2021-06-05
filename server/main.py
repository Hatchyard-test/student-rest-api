from fastapi import FastAPI
from routes.student_bp import student 


app = FastAPI()
app.include_router(student, prefix="/api", tags=["api"]) # Add router blueprints to app
