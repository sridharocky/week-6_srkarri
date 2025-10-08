import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

class Genius:
    def __init__(self, access_token=None):
        # Use provided token or fallback to environment variable
        self.access_token = access_token or os.getenv("ACCESS_TOKEN")
        if not self.access_token:
            raise ValueError("No ACCESS_TOKEN found. Put it in .env or pass to Genius().")
        self.base_url = "https://api.genius.com"

    def get_artist(self, search_term):
        search_url = f"{self.base_url}/search"
        params = {"q": search_term, "access_token": self.access_token}
        r = requests.get(search_url, params=params)
        r.raise_for_status()
        hits = r.json()["response"]["hits"]
        if not hits:
            return None
        artist_id = hits[0]["result"]["primary_artist"]["id"]
        artist_url = f"{self.base_url}/artists/{artist_id}"
        r2 = requests.get(artist_url, params={"access_token": self.access_token})
        r2.raise_for_status()
        return r2.json()["response"]["artist"]

    def get_artists(self, search_terms):
        rows = []
        for term in search_terms:
            artist = self.get_artist(term)
            if artist:
                rows.append({
                    "search_term": term,
                    "artist_name": artist.get("name"),
                    "artist_id": artist.get("id"),
                    "followers_count": artist.get("followers_count")
                })
            else:
                rows.append({
                    "search_term": term,
                    "artist_name": None,
                    "artist_id": None,
                    "followers_count": None
                })
        return pd.DataFrame(rows)
