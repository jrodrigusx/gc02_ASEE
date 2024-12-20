import connexion
import six

from ..models.recomendaciones_series import RecomendacionesSeries  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_visualizaciones as db


def recomendaciones_series_id_get(id):  # noqa: E501
    """Obtener las recomendaciones para un usario de series

     # noqa: E501

    :param id: ID de las recomendaciones de series
    :type id: str

    :rtype: RecomendacionesSeries
    """
    db.dbSerieRecomendations()



def recomendaciones_series_id_put(body, id):  # noqa: E501
    """Actualizar las recomendaciones de series

     # noqa: E501

    :param body: Datos para actualizar las recomendaciones de series
    :type body: dict | bytes
    :param id: ID de las recomendaciones de series
    :type id: str

    :rtype: None
    """
    return db.dbSerieRecomendations(id)
