import pandas as pd
import streamlit as st
from reviews.service import ReviewService
from movies.service import MovieService
from st_aggrid import AgGrid


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        reviews_df = pd.json_normalize(reviews)
        st.write('Lista de Avaliações:')
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid',
        )
    else:
        st.warning('Nenhuma Avaliacao encontrada.')

    st.title('Cadastrar Nova Avaliacao')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,  # para avancar de um em um
    )
    comment = st.text_area('Comentario')

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar as avaliacoes. Verifique os campos')
