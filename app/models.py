from pydantic import BaseModel

class Song(BaseModel):
    title: str
    artist: str
    duration: int
    audio_url: str
    thumbnail: str
    webpage_url: str