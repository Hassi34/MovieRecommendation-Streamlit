import streamlit as st 
st.set_page_config(
page_title="Copyright © 2021 Hasnain",
page_icon="🎢",
layout="wide",
initial_sidebar_state="expanded")

import pandas as pd
from requests.models import Response 
import pickle
import requests
import gzip

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    complete_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return complete_path
def recommender(movie) :
    movie_index = movies[movies['title'] == movie].index[0]
    distances= similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x : x[1])[1:7]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        #fetch_poster_from api
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names, recommended_movie_posters


with gzip.open ('movies.pickle.gz', 'rb') as f:
    movies = pickle.load(f) 
movies_list = movies['title'].values
with gzip.open ('similarity.pickle.gz', 'rb') as f:
    similarity = pickle.load(f)

st.title('Move Recomender System')
selected_movie_name = st.selectbox(
    'Select the movie of your choice', movies_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommender(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col2:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col3:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

st.header('Get the Code')
link = '[GitHub](https://github.com/Hassi34/MovieRecommendation-Streamlit.git)'
st.markdown(link, unsafe_allow_html=True)