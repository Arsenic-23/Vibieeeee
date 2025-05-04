# JioSaavn FastAPI Backend

This is a FastAPI backend for fetching songs from JioSaavn with an advanced search system.

## Requirements
- Python 3.8+
- Install dependencies using:

pip install -r requirements.txt

## Running the App
- Start the FastAPI server:

uvicorn app.main:app --reload

The app will be available at `http://127.0.0.1:8000`.

## API Endpoints

### /search?query=...
- **Query Parameter**: `query` (Song title or artist name)
- Returns the best-matched song's title, artist, duration, audio URL, and thumbnail.

Example response:
```json
{
"title": "Shape of You",
"artist": "Ed Sheeran",
"duration": 233,
"audio_url": "https://media.jiosaavn.com/hapi/song/abc123.mp3",
"thumbnail": "https://www.jiosaavn.com/thumbnail.jpg",
"webpage_url": "https://www.jiosaavn.com/song/abc123"
}

---

### **How it works:**
- **Smart Search**: Fuzzy matching using the `fuzzywuzzy` library ensures that even if the query is not exact (e.g., missing parts of the title, misspellings), it still returns the most relevant result.
- **JioSaavn API**: The system fetches songs using JioSaavn's API and pulls metadata like title, artist, duration, thumbnail, and MP3 URL.

---

### **Testing the API:**

1. **Run the app**:
   ```bash
   uvicorn app.main:app --reload

2. Test with a query:

Visit http://127.0.0.1:8000/search?query=Shape%20of%20You in your browser or use Postman to send a GET request.