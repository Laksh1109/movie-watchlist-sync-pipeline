def resolve_duplicate(title, year, search_func, fetch_func):
    results = search_func(title)
    if not results:
        return None
    if year:
        for movie in results:
            if movie.get("Year") == str(year):
                return fetch_func(movie.get("Title"), year)
    best_movie = None
    best_rating = 0

    for movie in results:
        data = fetch_func(movie.get("Title"))
        if not data:
            continue
        try:
            rating = float(data.get("imdbRating", 0))
        except:
            rating = 0

        if rating > best_rating:
            best_rating = rating
            best_movie = data
    return best_movie

def enrich_data(df, search_func, fetch_func):
    enriched = []

    for _, row in df.iterrows():
        title = row.get('title')
        if not title or str(title).strip() == "":
            continue
        year = row.get('year')
        movie = resolve_duplicate(
            title,
            year,
            search_func,
            fetch_func
        )

        if not movie:
            continue
        try:
            rating = float(movie.get("imdbRating", 0)) if movie.get("imdbRating") != "N/A" else 0
        except:
            rating = 0
        try:
            runtime = int(movie.get("Runtime").split()[0]) if movie.get("Runtime") != "N/A" else 0
        except:
            runtime = 0

        enriched.append({
            "title": movie.get("Title"),
            "rating": rating,
            "genre": movie.get("Genre"),
            "runtime": runtime,
            "year": movie.get("Year")
        })

    return enriched
