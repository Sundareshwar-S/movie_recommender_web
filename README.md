# 🎬 Movie Recommender System (Genre-Based)

## Live Deployed Link

You can access the live movie recommendation system at: https://movierecommenderweb-production.up.railway.app


---

## 📌 Overview

This project is a Flask-based web application that allows users to select their favorite movie genres and receive personalized movie recommendations. 
The recommendations are generated using preloaded datasets of movies and user ratings.

---

## 🧠 How It Works

### 1. **Data Loading**
- Movie metadata is loaded from `item.csv` (converted from MovieLens's `u.item`).
- Ratings are loaded from `ratings.csv` (converted from `u.data`).

### 2. **Genre-Based Filtering**
- The app presents users with genre checkboxes (e.g., Action, Romance).
- On form submission, the selected genres are used to filter movies tagged with those genres.

### 3. **Recommendation Logic**
- The filtered movies are joined with user ratings.
- Movies are scored using:
  - **Average Rating**
  - **Rating Count**
- The top 5 movies are returned as recommendations.

---

## 💻 Technology Stack

| Tool            | Use Case                          |
|-----------------|-----------------------------------|
| **Python**      | Backend logic and data wrangling  |
| **Flask**       | Web framework                     |
| **Pandas**      | Data loading, filtering, and analysis |
| **HTML/CSS**    | Frontend design                   |
| **Render**      | Deployment                        |

---

## 📁 Project Structure

```text
todo-list-app/
│
├── app.py            # Main Flask application
├── requirements.txt  # Python dependencies
├── start.sh          # Glitch startup script
├── .glitch.json      # Glitch configuration
│
├── templates/
│   └── index.html    # HTML template (Jinja2)
│
└── static/
    └── style.css     # CSS styling
---

## ✨ Features

- 🎯 Select one or more genres via checkboxes.
- 📊 Recommends movies based on ratings and popularity.
- 🧼 Clean, modern UI using HTML/CSS.
- 🚀 Deployed live using Render.

---

## 🤖 AI Assistance

This project was created with the assistance of **ChatGPT and Github Copilot** for:
- Logic planning and debugging.
- UI and UX improvements.
- Markdown documentation.

---
