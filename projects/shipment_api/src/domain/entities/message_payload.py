from pydantic import BaseModel

class MessagePayload(BaseModel):
    channel: str
    content: dict