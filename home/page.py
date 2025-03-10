import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatistica de Filmes')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Genero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Filmes por Genero',
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats['total_movies'])

    st.subheader('Quantidade de Files por Genero')
    for genre in movie_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader('Total de Avaliacoes Cadastradas:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Media Geral de Estrelas nas Avaliacoes:')
    st.write(movie_stats['average_stars'])
