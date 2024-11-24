import connexion
import six

from ..models.capitulo import Capitulo  # noqa: E501
from .. import util

from flask import request, jsonify
from ..... import dbconnection

def series_id_temporadas_temporada_id_capitulos_get(id, temporada_id):  # noqa: E501
    """Obtener todos los capítulos de una temporada específica

     # noqa: E501

    :param id: ID de la serie
    :type id: str
    :param temporada_id: ID de la temporada
    :type temporada_id: str

    :rtype: List[Capitulo]
    """
    return dbconnection.dbGetEpisodesOfSeason(id, temporada_id)
