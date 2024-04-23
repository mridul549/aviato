from pydantic import BaseModel

class Video(BaseModel):
    videoid: str
    title: str
    description: str
    channel: str
    publishedTime: str
    thumbnail: str
