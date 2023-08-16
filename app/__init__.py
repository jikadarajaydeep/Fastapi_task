from fastapi import FastAPI
from .auth import router as auth_router
from .posts import router as api_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(api_router, prefix="/posts")