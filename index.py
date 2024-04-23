from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncio
from routes.index import video
from service.youtube import fetchVideos

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(fetchVideos())
    try:
        yield  
    finally:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass  

app = FastAPI(lifespan=lifespan)
app.include_router(video)
