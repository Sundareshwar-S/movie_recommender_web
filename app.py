from flask import Flask, render_template, request
from genre_based_logic import get_genre_recommendations

app = Flask(__name__)

# List of available genres (based on item.csv inspection)
AVAILABLE_GENRES = [
    'Action', 'Adventure', 'Animation', "Children's", 'Comedy',
    'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
    'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
    'Thriller', 'War', 'Western'
]

@app.route('/')
def index():
    """Renders the main page with genre selection form."""
    return render_template('index.html', genres=AVAILABLE_GENRES)

@app.route('/recommend', methods=['POST'])
def recommend():
    """Handles form submission and displays recommendations."""
    selected_genres = request.form.getlist('genres')  # Get selected genres from the form
    recommendations, error = get_genre_recommendations(selected_genres)

    # Render the template with the results
    return render_template(
        'index.html',
        genres=AVAILABLE_GENRES,
        selected_genres=selected_genres,
        recommendations=recommendations,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')