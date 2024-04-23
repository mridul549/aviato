from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from routes.index import video, key
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

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video)
app.include_router(key)
