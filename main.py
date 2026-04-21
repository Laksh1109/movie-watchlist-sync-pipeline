from ingestion import load_watchlist
from api_client import search_movies, fetch_movie_data
from processing import enrich_data
from storage import init_db, insert_movies
from ranking import rank_movies
from export import export_playlist

# Step 1: Load CSV
df = load_watchlist("Want_to_Watch.csv")

# Step 2: Process + Enrich
data = enrich_data(df, search_movies, fetch_movie_data)


# Step 3: Store in DB
init_db()
insert_movies(data)

print("✅ Data saved to database")  

# Step 4: Ranking
ranked = rank_movies(data)

# Step 5: Top 5 recommendations
playlist = ranked[:5]

print("\n🎬 Weekend Playlist:")
for movie in playlist:
    print(movie['title'], "-", movie['rating'])

export_playlist(playlist)