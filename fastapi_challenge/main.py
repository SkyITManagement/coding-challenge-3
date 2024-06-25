from fastapi import FastAPI
# from pydantic import BaseModel

app = FastAPI()

#delete when ready to create the endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a Pydantic model for the request body with name, studying, and age

# Define a POST endpoint that receives Intern details and returns them
