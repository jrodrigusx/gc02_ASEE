import connexion
import six

from ..models.capitulo import Capitulo  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_contenidos as db

def series_id_temporadas_temporada_id_capitulos_get(id, temporada_id):  # noqa: E501
    """Obtener todos los capítulos de una temporada específica

     # noqa: E501

    :param id: ID de la serie
    :type id: str
    :param temporada_id: ID de la temporada
    :type temporada_id: str

    :rtype: List[Capitulo]
    """
    episodes = []
    for info in db.dbGetEpisodesOfSeason(id, temporada_id):
        episode = Capitulo(info[0], info[1], info[5], info[4], info[6], None)
        episodes.append(episode.to_dict())
    return episodes
