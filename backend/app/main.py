from fastapi import FastAPI
from starlette.requests import Request
import uvicorn
from fastapi.staticfiles import StaticFiles

from app.core import config
from app.core.session import SessionLocal
from app.core.routes import include_routes


def configure_static(main_app):
    main_app.mount("/static", StaticFiles(directory="app/static"), name="static")


def start_application():
    main_app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")
    configure_static(main_app)
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
