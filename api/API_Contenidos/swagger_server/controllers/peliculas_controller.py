import connexion
import six

from ..models.actor import Actor  # noqa: E501
from ..models.director import Director  # noqa: E501
from ..models.pelicula import Pelicula  # noqa: E501
from .. import util

from flask import request, jsonify
import dbconnection



def peliculas_genero_genero_get(genero):  # noqa: E501
    """Obtener todas las películas

     # noqa: E501

    :param genero: ID de la pelicula a buscar
    :type genero: str

    :rtype: List[Pelicula]
    """
    return dbconnection.dbGetMoviesByGenre(genero)


def peliculas_get():  # noqa: E501
    """Obtener todas las películas

     # noqa: E501


    :rtype: List[Pelicula]
    """
    return dbconnection.dbGetMovies()


def peliculas_id_actores_get(id):  # noqa: E501
    """Obtener los actores de una película específica

     # noqa: E501

    :param id: ID de la película
    :type id: str

    :rtype: List[Actor]
    """
    return dbconnection.dbGetActorsInMovie(id)


def peliculas_id_directores_get(id):  # noqa: E501
    """Obtener los directores de una película específica

     # noqa: E501

    :param id: ID de la película
    :type id: str

    :rtype: List[Director]
    """
    return dbconnection.dbGetMovieDirector(id)


def peliculas_id_get(id):  # noqa: E501
    """Obtener una pelicula por id

     # noqa: E501

    :param id: ID de la pelicula a buscar
    :type id: str

    :rtype: Pelicula
    """
    return dbconnection.dbGetMovieById(id)


def peliculas_titulo_titulo_get(titulo):  # noqa: E501
    """Obtener todas las películas que contengan el título

     # noqa: E501

    :param titulo: Título parcial de la película a buscar
    :type titulo: str

    :rtype: List[Pelicula]
    """
    return dbconnection.dbGetMoviesByTitle(titulo)