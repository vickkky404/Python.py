import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Set the path to the datasets folder
folder_path = r"D:\PROGRAM\PY Projects\MOVIE RECOMENDER\datasets"

# Load CSV files
credits_df = pd.read_csv(os.path.join(folder_path, "credits.csv"))
keywords_df = pd.read_csv(os.path.join(folder_path, "keywords.csv"))
movies_metadata_df = pd.read_csv(os.path.join(folder_path, "movies_metadata.csv"), low_memory=False)

# Convert 'id' to numeric
movies_metadata_df['id'] = pd.to_numeric(movies_metadata_df['id'], errors='coerce')
credits_df['id'] = pd.to_numeric(credits_df['id'], errors='coerce')
keywords_df['id'] = pd.to_numeric(keywords_df['id'], errors='coerce')

# it helps to merge the data sets
movies_df = movies_metadata_df.merge(credits_df, on="id", how="left")
movies_df = movies_df.merge(keywords_df, on="id", how="left")

# Select relevant columns
movies_df = movies_df[['id', 'title', 'overview', 'genres', 'keywords']]

# Fill missing values
movies_df['overview'] = movies_df['overview'].fillna('')

# TF-IDF Vectorization (Convert text to numerical data)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['overview'])


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


# Function to get movie recommendations
def recommend_movies(movie_title, num_recommendations=5):
    if movie_title not in movies_df['title'].values:
        return "Movie not found in database!"

    # Get movie index
    idx = movies_df[movies_df['title'] == movie_title].index[0]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies by similarity score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations + 1]

    # Get recommended movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return recommended movie titles
    return movies_df['title'].iloc[movie_indices].tolist()


# Example usage
movie_name = "Jumanji"  # Change this to any movie title from your dataset
print(f"Movies similar to '{movie_name}':", recommend_movies(movie_name))
