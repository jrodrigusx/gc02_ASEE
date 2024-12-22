import connexion
import six

from ..models.pelicula import Pelicula  # noqa: E501
from .. import util
from . import actores_controller, directores_controller

from flask import request, jsonify
from ... import dbconnection_contenidos as db


def peliculas_genero_genero_get(genero):  # noqa: E501
    """Obtener todas las películas

     # noqa: E501

    :param genero: ID de la pelicula a buscar
    :type genero: str

    :rtype: List[Pelicula]
    """
    movies = []
    for info in db.dbGetMoviesByGenre(genero):
        movie = Pelicula(info[0], info[1], info[2], info[3], peliculas_id_directores_get(info[0]), peliculas_id_actores_get(info[0]), info[5])
        movies.append(movie.to_dict())
    return movies


def peliculas_get():  # noqa: E501
    """Obtener todas las películas

     # noqa: E501


    :rtype: List[Pelicula]
    """
    movies = []
    for info in db.dbGetMovies():
        movie = Pelicula(info[0], info[1], info[2], info[3], peliculas_id_directores_get(info[0]), peliculas_id_actores_get(info[0]), info[5])
        movies.append(movie.to_dict())
    return movies


def peliculas_id_actores_get(id):  # noqa: E501
    """Obtener los actores de una película específica

     # noqa: E501

    :param id: ID de la película
    :type id: str

    :rtype: List[Actor]
    """
    actors = []
    for info in db.dbGetActorsInMovie(id):
        actor = actores_controller.actores_id_get(info[0])
        actors.append(actor)
    return actors


def peliculas_id_directores_get(id):  # noqa: E501
    """Obtener los directores de una película específica

     # noqa: E501

    :param id: ID de la película
    :type id: str

    :rtype: List[Director]
    """
    info = db.dbGetMovieDirector(id)
    director = directores_controller.directores_id_get(info[0])
    return director


def peliculas_id_get(id):  # noqa: E501
    """Obtener una pelicula por id

     # noqa: E501

    :param id: ID de la pelicula a buscar
    :type id: str

    :rtype: Pelicula
    """
    info = db.dbGetMovieById(id)
    movie = Pelicula(info[0], info[1], info[2], info[3], peliculas_id_directores_get(info[0]), peliculas_id_actores_get(info[0]), info[5])
    return movie.to_dict()


def peliculas_titulo_titulo_get(titulo):  # noqa: E501
    """Obtener todas las películas que contengan el título

     # noqa: E501

    :param titulo: Título parcial de la película a buscar
    :type titulo: str

    :rtype: List[Pelicula]
    """
    movies = []
    for info in db.dbGetMoviesByTitle(titulo):
        movie = Pelicula(info[0], info[1], info[2], info[3], peliculas_id_directores_get(info[0]), peliculas_id_actores_get(info[0]), info[5])
        movies.append(movie.to_dict())
    return movies