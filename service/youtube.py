import asyncio
from config.db import conn
from models.index import videos
from schemas.index import Video
import os
import httpx

async def fetchVideos():
    while True:
        await helper()
        await asyncio.sleep(10)

async def helper():
    transaction = conn.begin()  # Start transaction
    try:
        params = {
            'part': 'snippet',
            'q': 'cricket',
            'type': 'video',
            'order': 'date',
            'maxResults': 5,
            'key': "AIzaSyBb1ERlTO9MFo_THiJCiU8gI4rhy8MkGCg"
        }
        
        # async with httpx.AsyncClient() as client:
            # response = await client.get('https://www.googleapis.com/youtube/v3/search', params=params)

            # if response.status_code == 200:
            #     data = response.json()
            #     for item in data.get('items', []):
            #         video_id = item['id']['videoId']
            #         print(video_id)
            #         # Check if video already exists in the database
            #         existing_video = conn.execute(videos.select().where(videos.c.videoid == video_id)).fetchone()
                    
            #         if not existing_video:
            #             # Insert new video into database
            #             conn.execute(videos.insert().values(
            #                 videoid=video_id,
            #                 title=item['snippet']['title'],
            #                 description=item['snippet']['description'],
            #                 publishedTime=item['snippet']['publishTime'],
            #                 channel=item['snippet']['channelTitle'],
            #                 thumbnail=item['snippet']['thumbnails']['default']['url']
            #             ))
                
            #     transaction.commit()  # Commit after all inserts
            # else:
            #     print(f"Failed to fetch data: {response.status_code}, {response.text}")
                
    except Exception as err:
        print(f"An error occurred: {err}")
        transaction.rollback()  
    finally:
        if not transaction.is_active:
            transaction.close()  
