from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional,List
class Student(BaseModel):
  name:str
  age:str
  married:Optional[List[str]]=None
  
def showingnameandage(student:Student):
  print("working",student.age,student.name)
student={'name':'bilal','age':'19'}
student1=Student(**student)
showingnameandage(student1)






# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/getlost")
# def working():
#     raise HTTPException(status_code=201,detail="working perfectly")
#     return {"agayabnharaway"}