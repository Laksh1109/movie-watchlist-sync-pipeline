import pandas as pd

def export_playlist(movies):
    df = pd.DataFrame(movies)
    df.to_csv("Weekend_Playlist.csv", index=False)
    print("📄 Playlist exported to Weekend_Playlist.csv")