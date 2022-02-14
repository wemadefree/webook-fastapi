import uvicorn
from core.config import config
from fastapi import FastAPI
from app.views.home import home_router


def init_routers(app: FastAPI) -> None:
    app.include_router(home_router)


def create_app() -> FastAPI:
    app = FastAPI(
        title="WeBook FastAPI",
        description="REST based solution in FastAPI for WeBook project",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
    )
    init_routers(app=app)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "production" else False,
        workers=1,
    )
