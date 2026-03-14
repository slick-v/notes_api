from fastapi import FastAPI
from .database import *
from .router import notes,users



Base.metadata.create_all(bind=engine)

app =FastAPI()

app.include_router(notes.router)
app.include_router(users.router)



@app.get("/")
def home():
    return {"Status" : "Ok!"}