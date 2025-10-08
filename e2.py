from apputil import Genius
import json

# exercise_2.py
g = Genius()  # loads token from .env
print("Exercise 2...\n")
artist = g.get_artist("Radiohead")
print("Name:", artist["name"])
print("Followers:", artist["followers_count"])
print("URL:", artist["url"])
