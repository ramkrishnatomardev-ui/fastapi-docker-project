from fastapi import FastAPI

app = FastAPI(title="My FastAPI Project")


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
