from fastapi import FastAPI
from routes.index import video

app = FastAPI()

app.include_router(video)