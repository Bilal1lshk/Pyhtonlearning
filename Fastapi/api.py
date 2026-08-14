from fastapi import FastAPI,HTTPException
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/getlost")
def working():
    raise HTTPException(status_code=201,detail="working perfectly")
    return {"agayabnharaway"}