import streamlit as st
import pickle
import pandas as pd
import streamlit

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
movie_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in movie_indices[1:6]:  # top 5 similar movies
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movie_list
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
