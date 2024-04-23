from fastapi import APIRouter, Query
from sqlalchemy import select, func
from config.db import conn
from models.index import keys

key = APIRouter()
@key.post('/key/{key_id}')
async def add_key(key_id: str):
    transaction = conn.get_transaction()

    try:
        query = select(keys).where(keys.c.keyValue == key_id)
        result = conn.execute(query).fetchone()
        
        if result is None:

            conn.execute(keys.insert().values(keyValue=key_id, active=True))
            transaction.commit()  # Commit the changes
            return {"message": "Key added"}
        else:
            return {"error": "Key already exists"}, 409
    except Exception as e:
        # Rollback the transaction on error
        transaction.rollback()
        raise e
