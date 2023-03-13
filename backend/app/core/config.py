import os

PROJECT_NAME = "webook-fastapi"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

GRAPH_CLIENT_ID = os.getenv("GRAPH_CLIENT_ID")
GRAPH_CLIENT_SECRET = os.getenv("GRAPH_CLIENT_SECRET")
GRAPH_AUTHORITY = os.getenv("GRAPH_AUTHORITY")

API_V1_STR = "/api/v1"
