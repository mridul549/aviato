from sqlalchemy import create_engine, MetaData
import os

engine = create_engine(os.getenv("MYSQL_URI"))
meta = MetaData()
conn = engine.connect()
