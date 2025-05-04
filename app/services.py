import httpx
from app.models import Song
from typing import List

async def fetch_jiosaavn_results(query: str) -> List[Song]:
    url = f"https://www.jiosaavn.com/api.php?__call=search.get_results&query={query}&count=10"
    params = {"__call": "search.get_results", "query": query, "count": "10"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    data = response.json()

    if data["status"] == "ok":
        songs = []
        for result in data.get("results", {}).get("songs", []):
            song = Song(
                title=result["song"]["title"],
                artist=result["song"]["primary_artists"],
                duration=result["song"]["duration"],
                audio_url=result["song"]["media_url"],
                thumbnail=result["song"]["image"],
                webpage_url=f"https://www.jiosaavn.com/song/{result['song']['id']}",
            )
            songs.append(song)

        return songs

    return []