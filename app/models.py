from pydantic import BaseModel

class AudioInfo(BaseModel):
    title: str
    channel: str
    duration: int
    audio_url: str
    thumbnail: str
    webpage_url: str