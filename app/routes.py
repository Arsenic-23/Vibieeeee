from fastapi import APIRouter, HTTPException
from app.services import fetch_jiosaavn_results
from app.utils import smart_search
from app.models import Song

router = APIRouter()

@router.get("/search", response_model=Song)
async def search_song(query: str):
    songs = await fetch_jiosaavn_results(query)
    if not songs:
        raise HTTPException(status_code=404, detail="No songs found")

    # Smart search to find the best match
    best_match_song = smart_search(query, songs)
    if best_match_song:
        return best_match_song
    
    raise HTTPException(status_code=404, detail="No matching song found")