from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.routes.watch.api import router as watch_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(watch_router)

@app.get('/')
async def index():
    return "hellody log-server"

if __name__ == "__main__":
    uvicorn.run("main:app", host = '127.0.0.1', port = 80, reload=True)