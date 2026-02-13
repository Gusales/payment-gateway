from fastapi import FastAPI

from app.config.env import env

app = FastAPI(
    title=env.app_name,
)

@app.get('/')
def get_hello():
    return { "message": "Hello World" }