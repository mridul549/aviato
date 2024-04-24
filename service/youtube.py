import asyncio
from config.db import conn
from models.index import videos, keys
from schemas.index import Video, Key
import os
import httpx
from dotenv import load_dotenv
load_dotenv()

async def fetchVideos():
    while True:
        await helper()
        await asyncio.sleep(1000)

async def helper():
    transaction = conn.begin()  # Start transaction

    try:
        apikeys = conn.execute(keys.select()).fetchall()

        for key in apikeys:
            params = {
                'part': 'snippet',
                'q': 'cricket',
                'type': 'video',
                'order': 'date',
                'maxResults': 50,
                'publishedAfter': '2023-04-20T00:00:00Z', # published after Thu Apr 20 2023 05:30:00 GMT+0530
                'key': key[1]
            }
            
            currentStatus = key[2]

            async with httpx.AsyncClient() as client:
                response = await client.get('https://www.googleapis.com/youtube/v3/search', params=params)

                if response.status_code == 200:
                    data = response.json()
                    for item in data.get('items', []):
                        video_id = item['id']['videoId']

                        # Check if video already exists in the database
                        existing_video = conn.execute(videos.select().where(videos.c.videoid == video_id)).fetchone()
                        
                        if not existing_video:
                            # Insert new video into database
                            conn.execute(videos.insert().values(
                                videoid=video_id,
                                title=item['snippet']['title'],
                                description=item['snippet']['description'],
                                publishedTime=item['snippet']['publishTime'],
                                channel=item['snippet']['channelTitle'],
                                thumbnail=item['snippet']['thumbnails']['high']['url']
                            ))  
                    if currentStatus == 0:
                        conn.execute(keys.update().values(
                            active=True
                        ).where(keys.c.keyValue == key[1]))
                    
                    transaction.commit()

                else:
                    if currentStatus == 1:
                        conn.execute(keys.update().values(
                            active=False
                        ).where(keys.c.keyValue == key[1]))
                        transaction.commit()

    except Exception as err:
        print(f"An error occurred: {err}")
        transaction.rollback()  
