from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

videos = Table(
    'videos', meta,
    Column('id', Integer, primary_key=True),
    Column('videoid', String(255)),
    Column('title', String(255)),
    Column('description', String(255)),
    Column('channel', String(255)),
    Column('publishedTime', String(255)),
    Column('thumbnail', String(2048))
)