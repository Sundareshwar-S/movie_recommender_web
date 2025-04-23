

import pandas as pd

# Define the column names
columns = [
    "movie_id", "title", "release_date", "video_release_date", "IMDb_URL",
    "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
    "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
]

# Read the file using '|' as the separator
df = pd.read_csv('u.item', sep='|', encoding='latin-1', names=columns)

# Save it as a CSV
df.to_csv('item.csv', index=False)

print("Conversion complete! Saved as movies.csv.")
