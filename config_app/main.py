from fastapi import FastAPI
from api.routes.config_router import router

app = FastAPI()

app.include_router(router)