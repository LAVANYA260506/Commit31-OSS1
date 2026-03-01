from fastapi import FastAPI,Depends
import uvicorn
from pydantic import BaseModel
from sqlalchemy.orm import Session


from .database import engine, Base , SessionLocal
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

class TaskCreate(BaseModel):
    title:str
    description : str
    status:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/task")
def create_task(task:TaskCreate,db:Session = Depends(get_db)):
    new_task = models.Task(title= task.title , description =task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task                

@app.get("/")
def home():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)