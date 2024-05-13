from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import logging
import logging.handlers

#logging.basicConfig(level="INFO",filename="logging.log",filemode="w") 

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")
@app.get("/file", response_class=FileResponse)
def read_file():
    return "index.html"

@app.get("/users/{id}/{key}")
def users(id, key):
    return {"user_id" : id, "user_key" : key}

