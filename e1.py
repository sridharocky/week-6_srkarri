from apputil import Genius
import json

print("Exercise 1...\n")
# exercise_1.py
g = Genius()  # loads token from .env
print("Access token loaded (first 6 chars):", g.access_token[:6] + "..." )


print("✅ Genius object created successfully!")
print("Stored access token:", g.access_token)



