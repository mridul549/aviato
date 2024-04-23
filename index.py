from fastapi import FastAPI
from routes.index import video
import asyncio
from service.youtube import fetchVideos

app = FastAPI()

app.include_router(video)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(fetchVideos())
