from fuzzywuzzy import process

# Function to perform fuzzy search for the best match
def smart_search(query, songs):
    """Match query with song title and artist using fuzzy logic"""
    song_titles = [f"{song['title']} - {song['artist']}" for song in songs]
    best_match = process.extractOne(query, song_titles)
    
    if best_match:
        # Return the song with the highest match score
        match_index = song_titles.index(best_match[0])
        return songs[match_index]
    
    return None