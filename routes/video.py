from fastapi import APIRouter, Query
from sqlalchemy import select
from config.db import conn
from models.index import videos

video = APIRouter()

@video.get('/')
async def getVideos(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1)
):
    # Calculate offset
    offset = (page - 1) * page_size

    # Prepare the query with ordering and pagination
    statement = (
        select(videos)
        .order_by(videos.c.publishedTime.desc()) 
        .limit(page_size)
        .offset(offset)
    )

    result = conn.execute(statement).fetchall()

    # Convert result to list of dictionaries
    videos_list = [dict(row._mapping) for row in result]
    return videos_list
