import connexion
import six

from ..models.visualizaciones_peliculas import VisualizacionesPeliculas  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_visualizaciones as db


def visualizaciones_peliculas_id_get(id):  # noqa: E501
    """las visualizaciones de una pelicula

     # noqa: E501

    :param id: ID de las visualizaciones de una película
    :type id: str

    :rtype: VisualizacionesPeliculas
    """
    views = VisualizacionesPeliculas(None, id, db.dbGetMovieViews(id))
    return views


def visualizaciones_peliculas_id_put(body, id):  # noqa: E501
    """Actualizar las visualizaciones de una película

     # noqa: E501

    :param body: Datos para actualizar las visualizaciones de la película
    :type body: dict | bytes
    :param id: ID de las visualizaciones de una película
    :type id: str

    :rtype: None
    """
    db.dbUpdateMovieViews(None, id)
    # supongo que el id de las visualizaciones coincide con el id del usuario
    if connexion.request.is_json:
        body = VisualizacionesPeliculas.from_dict(connexion.request.get_json())  # noqa: E501
        view = body.num_visualizaciones
        
        if db.dbUpdateMovieViews(id, id, view):
            return {"mensaje": "Visualizaciones actualizadas correctamente"}, 200
        else:
            return {"error": "No se han podido actualizar las visualizaciones"}, 400
    return {"error": "Solicitud inválida"}, 400