from fastapi import APIRouter
from config.db import conn
from models.index import videos
from schemas.index import Video
from controllers.video import *

video = APIRouter()

@video.get('/')
async def getVideos():
    return getVideos()