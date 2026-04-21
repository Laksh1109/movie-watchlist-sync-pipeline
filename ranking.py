def rank_movies(movies):

    # 🔥 filter unwatched movies
    movies = [m for m in movies if m.get("watched", 0) == 0]

    ranked = []

    for m in movies:
        rating = m['rating']
        runtime = m['runtime']

        score = rating + (1 / runtime if runtime else 0)

        m['score'] = score
        ranked.append(m)

    ranked.sort(key=lambda x: x['score'], reverse=True)

    return ranked