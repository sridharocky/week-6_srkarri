from apputil import Genius
import json

g = Genius()  # loads token from .env
print("Exercise 3...\n")
# exercise_3.py

df = g.get_artists(['Rihanna', 'Tycho', 'Seal', 'U2'])
print(df)
df.to_csv("artists_test_output.csv", index=False)