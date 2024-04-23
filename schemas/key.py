from pydantic import BaseModel

class Key(BaseModel):
    keyValue: str
    active: bool
