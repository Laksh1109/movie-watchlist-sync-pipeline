import pandas as pd
import requests

API_KEY = "7989f01f"

# csv file load kar rahe
df = pd.read_csv("Want_to_Watch.csv")

movies = []

# har movie ke liye loop
for i, row in df.iterrows():
    name = row["title"]

    print("checking movie:", name)

    # api call
    url = f"http://www.omdbapi.com/?t={name}&apikey={API_KEY}"
    res = requests.get(url)
    movie = res.json()

    # agar movie nahi mili toh skip
    if movie.get("Response") == "False":
        print("not found:", name)
        continue

    # rating handle
    rating = movie.get("imdbRating")
    if rating == "N/A":
        rating = 0
    else:
        rating = float(rating)

    # runtime handle
    runtime = movie.get("Runtime")
    if runtime == "N/A":
        runtime = 0
    else:
        runtime = int(runtime.split()[0])

    # data store kar rahe list me
    movies.append({
        "title": movie.get("Title"),
        "rating": rating,
        "genre": movie.get("Genre"),
        "runtime": runtime,
        "year": movie.get("Year")
    })

# simple ranking logic (rating + short movie bonus)
for m in movies:
    if m["runtime"] != 0:
        m["score"] = m["rating"] + (1 / m["runtime"])
    else:
        m["score"] = m["rating"]

# sort kar diya best se worst
movies.sort(key=lambda x: x["score"], reverse=True)

# top 5 movies
top_movies = movies[:5]

print("\nWeekend Playlist: ")
for m in top_movies:
    print(m["title"], "->", m["rating"])

# csv me save
pd.DataFrame(top_movies).to_csv("Weekend_Playlist.csv", index=False)

print("Done")
