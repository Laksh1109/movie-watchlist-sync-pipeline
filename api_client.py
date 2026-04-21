import requests
API_KEY = "7989f01f"
def fetch_movie_data(title, year=None):
    title = str(title).replace(" ", "+")
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    if year:
        url += f"&y={year}"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "False":
            return None
        return data
    except Exception as e:
        print("Error:", e)
        return None

def search_movies(title):
    title = str(title).replace(" ", "+")
    url = f"http://www.omdbapi.com/?s={title}&apikey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("Response") == "False":
            return []
        return data.get("Search", [])
    except Exception as e:
        print("Error:", e)
        return []
