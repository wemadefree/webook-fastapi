import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app.core.docs import main_description, tags_metadata
from app.core.session import SessionLocal
from app.core.routes import include_routes
from app.users.auth import get_current_active_user,  get_current_user_from_token
from app.users.schemas import User


def start_application():
    #main_app = FastAPI(title="WeBook API", description=main_description, docs_url="/api/docs", openapi_url="/api", openapi_tags=tags_metadata)
    main_app = FastAPI(
        title="WeBook API",
        description=main_description,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        openapi_tags=tags_metadata
    )

    main_app.mount("/screendisplay", StaticFiles(directory="./app/screendisplay"), name="screendisplay")
    main_app.mount("/static", StaticFiles(directory="./app/webapp/static"), name="static")
    include_routes(main_app)
    return main_app


app = start_application()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)


@app.get("/api/docs", include_in_schema=False)
async def get_swagger_documentation(user: User = Depends(get_current_user_from_token)):
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="docs")


@app.get("/api/redoc", include_in_schema=False)
async def get_redoc_documentation(user: User = Depends(get_current_user_from_token)):
    return get_redoc_html(openapi_url="/api/openapi.json", title="docs")


@app.get("/api/openapi.json", include_in_schema=False)
async def openapi(user: User = Depends(get_current_user_from_token)):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)
