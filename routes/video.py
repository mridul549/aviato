from fastapi import APIRouter
from config.db import conn
from models.index import videos
from schemas.index import Video

video = APIRouter()

@video.get('/')
async def getVideos():
    return conn.execute(videos.select()).fetchall()
