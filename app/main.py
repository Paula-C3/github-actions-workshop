from fastapi import FastAPI         #type:ignore
from pydantic import BaseModel      #type:ignore
from app.calculator import sum, subtract, multiply

app = FastAPI()

class OperationInput(BaseModel):
    a: int
    b: int

@app.post("/add")
def add(data: OperationInput):
    return {"result": sum(data.a, data.b)}

@app.post("/subtract")
def subtract_numbers(data: OperationInput):
    return {"result": subtract(data.a, data.b)}

@app.post("/multiply")
def multiply_numbers(data: OperationInput):
    return {"result": multiply(data.a, data.b)}

