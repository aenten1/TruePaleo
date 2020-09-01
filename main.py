from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import sqlalchemy
from sqlalchemy.orm import Session
#from pydantic import BaseModel
#from database import SessionLocal, engine

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
        })

#this is a test of git
