import random

from fastapi import FastAPI

app = FastAPI(title="GitHub Playground API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to the GitHub Playground repository!",
        "repository_purpose": "Practice and experiment with GitHub features safely.",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/random-number")
def random_number() -> dict[str, int]:
    return {"number": random.randint(1, 100)}


@app.get("/echo")
def echo(message: str = "hello") -> dict[str, str]:
    return {"message": message}
