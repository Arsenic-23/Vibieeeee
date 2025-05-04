from fastapi import FastAPI, HTTPException, Query
from app.services import fetch_audio_info

app = FastAPI(title="YouTube Audio Stream API")

@app.get("/audio")
async def get_audio(video_id: str = Query(..., min_length=11, max_length=20)):
    try:
        result = fetch_audio_info(video_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))