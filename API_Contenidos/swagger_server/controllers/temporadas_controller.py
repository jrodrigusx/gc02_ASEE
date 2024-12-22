import connexion
import six

from . import capitulos_controller

from ..models.temporada import Temporada  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_contenidos as db

def series_id_temporadas_get(id):  # noqa: E501
    """Obtener todas las temporadas de una serie

     # noqa: E501

    :param id: ID de la serie
    :type id: str

    :rtype: List[Temporada]
    """
    seasons = []
    for info in db.dbGetSeasonsOfSerie(id):
        season = Temporada(info[0], info[2], info[3], capitulos_controller.series_id_temporadas_temporada_id_capitulos_get(id, info[0]))
        seasons.append(season.to_dict())
    return seasons
