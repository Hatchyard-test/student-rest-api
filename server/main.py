from fastapi import FastAPI
from routes.student_bp import student 
import uvicorn

app = FastAPI()
app.include_router(student, prefix="/api", tags=["api"]) # Add router blueprints to app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)