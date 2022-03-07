from fastapi import FastAPI
from starlette.requests import Request
import uvicorn
from fastapi.staticfiles import StaticFiles

from app.core.docs import main_description, tags_metadata
from app.core.session import SessionLocal
from app.core.routes import include_routes


def start_application():
    main_app = FastAPI(title="WeBook API", description=main_description, docs_url="/api/docs", openapi_url="/api", openapi_tags=tags_metadata)
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
