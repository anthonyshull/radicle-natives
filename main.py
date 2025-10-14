from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from surrealdb import Surreal

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def hello():
    """Returns a friendly greeting."""
    return "hello, world! i can connect to surrealdb."