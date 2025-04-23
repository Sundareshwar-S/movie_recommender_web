import pandas as pd
import os

# Paths (same dir as app.py assumed)
ITEM_FILE = 'item.csv'
RATINGS_FILE = 'ratings.csv'

# Load datasets
try:
    item_df = pd.read_csv(ITEM_FILE)
    ratings_df = pd.read_csv(RATINGS_FILE)
except Exception as e:
    print(f"Error loading data: {e}")
    item_df = pd.DataFrame()
    ratings_df = pd.DataFrame()

# --- Recommendation Logic ---
def get_genre_recommendations(selected_genres, max_results=5):
    """Returns up to 5 top-rated movies matching the selected genres."""
    if item_df.empty or ratings_df.empty:
        return None, "Movie or ratings data could not be loaded."

    if not selected_genres:
        return None, "Please select at least one genre."

    # Filter movies by selected genres
    genre_mask = item_df[selected_genres].any(axis=1)  # Check if any selected genre column is 1
    filtered_movies = item_df[genre_mask]

    if filtered_movies.empty:
        return None, f"No movies found for genres: {', '.join(selected_genres)}"

    # Merge filtered movies with ratings
    movie_ratings = pd.merge(ratings_df, filtered_movies, left_on='movieId', right_on='movie_id')

    # Aggregate ratings: calculate average rating and count of ratings
    aggregated = movie_ratings.groupby(['movie_id', 'title']).agg(
        avg_rating=('rating', 'mean'),
        rating_count=('rating', 'count')
    ).reset_index()

    # Sort movies by average rating and rating count
    top_movies = aggregated.sort_values(by=['avg_rating', 'rating_count'], ascending=[False, False]).head(max_results)

    return top_movies.to_dict('records'), None