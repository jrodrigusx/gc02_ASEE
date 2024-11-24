import connexion
import six

from ..models.temporada import Temporada  # noqa: E501
from .. import util

from flask import request, jsonify
from ..... import dbconnection

def series_id_temporadas_get(id):  # noqa: E501
    """Obtener todas las temporadas de una serie

     # noqa: E501

    :param id: ID de la serie
    :type id: str

    :rtype: List[Temporada]
    """
    return dbconnection.dbGetSeasonsOfSerie(id)
