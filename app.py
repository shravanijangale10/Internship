import streamlit as st
import pickle

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ==========================
# LOAD FILES
# ==========================

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ==========================
# TITLE
# ==========================

st.title("🎬 Movie Recommendation System")

st.markdown(
    "Get movie recommendations based on your favorite movie using Machine Learning."
)

st.markdown("---")

# ==========================
# MOVIE LIST
# ==========================

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Select a Movie",
    movie_list
)

# ==========================
# RECOMMEND FUNCTION
# ==========================

def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies

# ==========================
# BUTTON
# ==========================

if st.button("🎥 Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.success("Top 5 Recommended Movies")

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Scikit-learn")