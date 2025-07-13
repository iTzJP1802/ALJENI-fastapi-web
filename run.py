from fastapi import FastAPI
from app.main import app as application

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("run:application", host="127.0.0.1", port=8000, reload=True)
