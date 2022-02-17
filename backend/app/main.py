from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn

from app.api.api_v1.endpoints.users import users_router
from app.api.api_v1.endpoints.auth import auth_router
from api.api_v1.endpoints.location import location_router

from app.core import config
from app.core.session import SessionLocal
from app.core.auth import get_current_active_user


app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])

app.include_router(
    location_router,
    prefix="/api/v1",
    tags=["locations"],
    dependencies=[Depends(get_current_active_user)],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)