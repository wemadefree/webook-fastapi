from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


base_router = b = APIRouter()

#templates = Jinja2Templates(directory="app/templates")


#@b.get("/", response_class=HTMLResponse)
#async def root(request: Request):
#    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@b.get("/api",)
def login():
    return 'Hello, World!'