from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",  # Example: Frontend running on localhost:3000
    "https://yourfrontenddomain.com",  # Example: Production frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins (use ["*"] for all origins)
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Allows only specified request methods
    allow_headers=["X-Requested-With", "Content-Type"],  # Allows only specified headers
)


class HealthStatus(BaseModel):
    status: str

@app.get("/health", response_model=HealthStatus)
async def health_check():
    """
    Health Check Endpoint
    Returns the status of the API.
    """
    return {"status": "UP"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    Greet Endpoint
    Returns a greeting message to the user based on the provided name.
    """
    return {"message": f"Hello, {name}!"}
