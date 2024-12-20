import connexion
import six

from ..models.recomendaciones_peliculas import RecomendacionesPeliculas  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_visualizaciones as db

def recomendaciones_peliculas_id_get(id):  # noqa: E501
    """Obtener las recomendaciones para un usario de películas

     # noqa: E501

    :param id: ID de las recomendaciones de peliculas
    :type id: str

    :rtype: RecomendacionesPeliculas
    """
    movies = []
    for info in db.dbMovieRecomendations():
        movie = Pelicula(info[0], info[1], info[2], info[3], peliculas_id_directores_get(info[0]), peliculas_id_actores_get(info[0]), info[5])
        movies.append(movie.to_dict())
    return movies


def recomendaciones_peliculas_id_put(body, id):  # noqa: E501
    """Actualizar las recomendaciones de películas

     # noqa: E501

    :param body: Datos para actualizar las recomendaciones de películas
    :type body: dict | bytes
    :param id: ID de las recomendaciones de películas
    :type id: str

    :rtype: None
    """
    return db.dbSerieRecomendations(id)
