from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.api.api_v1.endpoints.auth import login_for_access_token
from app.core.session import get_session
from app.webapp.forms import LoginForm
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
login_router = log = APIRouter(include_in_schema=False)


@log.get("/login", response_class=HTMLResponse)
def login(request: Request):
    #return {"access_token": "fgfgfg", "token_type": "bearer", "request": request.headers}
    return templates.TemplateResponse("/auth/login.html", {"request": request})


@log.post("/login")
async def login(request: Request, db: Session = Depends(get_session)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = templates.TemplateResponse("auth/login.html", form.__dict__)
            print(form.__dict__)
            login_for_access_token(response=response, form_data=form, db=db)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)