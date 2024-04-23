from sqlalchemy import Table, Column, Integer, String, Boolean
from config.db import meta

keys = Table(
    'apikeys', meta,
    Column('id', Integer, primary_key=True),
    Column('keyValue', String(100), nullable=False),
    Column('active', Boolean, default=True)
)