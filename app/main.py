from fastapi import FastAPI
from .database import *
from .router import notes



Base.metadata.create_all(bind=engine)

app =FastAPI()

app.include_router(notes.router)



@app.get("/")
def home():
    return {"Status" : "Ok!"}