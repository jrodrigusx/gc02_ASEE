import connexion
import six

from ..models.recomendaciones_peliculas import RecomendacionesPeliculas  # noqa: E501
from .. import util

from flask import request, jsonify
from ..... import dbconnection

def recomendaciones_peliculas_id_get(id):  # noqa: E501
    """Obtener las recomendaciones para un usario de películas

     # noqa: E501

    :param id: ID de las recomendaciones de peliculas
    :type id: str

    :rtype: RecomendacionesPeliculas
    """

    return dbconnection.dbMovieRecomendations()


def recomendaciones_peliculas_id_put(body, id):  # noqa: E501
    """Actualizar las recomendaciones de películas

     # noqa: E501

    :param body: Datos para actualizar las recomendaciones de películas
    :type body: dict | bytes
    :param id: ID de las recomendaciones de películas
    :type id: str

    :rtype: None
    """
    return dbconnection.dbSerieRecomendations(id)
