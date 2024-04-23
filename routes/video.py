from fastapi import APIRouter, Query
from sqlalchemy import select, func
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

    # Prepare the query for videos with ordering and pagination
    videos_query = (
        select(videos)
        .order_by(videos.c.publishedTime.desc()) 
        .limit(page_size)
        .offset(offset)
    )

    # Prepare the query for total count
    count_query = select(func.count()).select_from(videos)

    # Execute queries
    result = conn.execute(videos_query).fetchall()
    total_count = conn.execute(count_query).scalar()

    # Convert result to list of dictionaries
    videos_list = [dict(row._mapping) for row in result]

    # Return videos and total count
    return {"videos": videos_list, "total_count": total_count}
