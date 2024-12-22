import connexion
import six

from ..models.visualizaciones_series import VisualizacionesSeries  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_visualizaciones as db


def visualizaciones_series_id_get(id):  # noqa: E501
    """Obtener las visualizaciones de una Serie

     # noqa: E501

    :param id: ID de las visualizaciones de una serie
    :type id: str

    :rtype: VisualizacionesSeries
    """
    try:
        visualizacion = db.dbGetSerieViews(id) # Supongo que esta función existe en `dbconnection`.
        if visualizacion:
            return jsonify(visualizacion), 200
        return {"error": "Visualizaciones de la serie no disponibles"}, 404
    except Exception as e:
        return {"error": f"Error al obtener visualizaciones de la serie: {str(e)}"}, 500


def visualizaciones_series_id_put(body, id):  # noqa: E501
    """Actualizar las visualizaciones de una serie

     # noqa: E501

    :param body: Datos para actualizar las visualizaciones de la serie
    :type body: dict | bytes
    :param id: ID de las visualizaciones de una serie
    :type id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = VisualizacionesSeries.from_dict(connexion.request.get_json())  # noqa: E501
        view = body.num_visualizaciones
        
        if db.dbUpdateSerieViews(id, id, view):
            return {"mensaje": "Visualizaciones actualizadas correctamente"}, 200
        else:
            return {"error": "No se han podido actualizar las visualizaciones"}, 400  
    return {"error": "Solicitud inválida"}, 400
