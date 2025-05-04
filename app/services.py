from yt_dlp import YoutubeDL

def fetch_audio_info(video_id: str):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'quiet': True,
        'format': 'ba/bestaudio/best',
        'skip_download': True,
        'noplaylist': True,
        'no_warnings': True,
        'cachedir': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "channel": info.get("channel"),
        "duration": info.get("duration"),
        "audio_url": info.get("url"),
        "thumbnail": info.get("thumbnail"),
        "webpage_url": info.get("webpage_url"),
    }