from fastapi import APIRouter, status
from fastapi import Depends
from fastapi import HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.api.api_v1.endpoints.auth import login as get_token_for_login
from app.core.session import get_session
from app.webapp.forms import LoginForm
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
login_router = log = APIRouter(include_in_schema=False)


@log.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("/auth/login.html", {"request": request})


@log.post("/login")
async def login(request: Request, db: Session = Depends(get_session)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            token = get_token_for_login(form_data=form, db=db)
            response = RedirectResponse(url="/api/docs", status_code=status.HTTP_303_SEE_OTHER)
            response.set_cookie(
                key="access_token",
                value=f"Bearer {token.get('access_token')}",
                httponly=True
            )
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)