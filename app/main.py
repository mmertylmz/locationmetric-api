from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.endpoints import router as api_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http:localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}