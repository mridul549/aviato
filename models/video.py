from sqlalchemy import Table, Column, Integer, String, Index
from config.db import meta

videos = Table(
    'videos', meta,
    Column('id', Integer, primary_key=True),
    Column('videoid', String(255), unique=True),  
    Column('title', String(255)),
    Column('description', String(255)),
    Column('channel', String(255)),
    Column('publishedTime', String(255)), 
    Column('thumbnail', String(2048)),
    # Adding an index to the publishedTime column
    Index('idx_published_time', 'publishedTime')
)