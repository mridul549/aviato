from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(os.getenv("MYSQL_URI"))
meta = MetaData()
conn = engine.connect()
