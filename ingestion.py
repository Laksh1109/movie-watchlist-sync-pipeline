import pandas as pd

def load_watchlist(Want_to_Watch):
    df = pd.read_csv(Want_to_Watch)
    return df