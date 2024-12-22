import connexion
import six

from . import actores_controller, temporadas_controller

from ..models.actor import Actor  # noqa: E501
from ..models.director import Director  # noqa: E501
from ..models.serie import Serie  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_contenidos as db

def series_genero_genero_get(genero):  # noqa: E501
    """Obtener una serie por genero

     # noqa: E501

    :param genero: Series con el genero a buscar
    :type genero: str

    :rtype: List[Serie]
    """
    series = []
    for info in db.dbGetSeriesByGenre(genero):
        serie = Serie(info[0], info[1], info[2], info[3], series_id_actores_get(info[0]), temporadas_controller.series_id_temporadas_get(info[0]))
        series.append(serie.to_dict())
    return series



def series_get():  # noqa: E501
    """Obtener todas las series

     # noqa: E501


    :rtype: List[Serie]
    """
    series = []
    for info in db.dbGetSeries():
        serie = Serie(info[0], info[1], info[2], info[3], series_id_actores_get(info[0]), temporadas_controller.series_id_temporadas_get(info[0]))
        series.append(serie.to_dict())
    return series


def series_id_actores_get(id):  # noqa: E501
    """Obtener actores de una serie específica

     # noqa: E501

    :param id: ID de la serie
    :type id: str

    :rtype: List[Actor]
    """
    actors = []
    for info in db.dbGetActorsInSerie(id):
        actor = actores_controller.actores_id_get(info[0])
        actors.append(actor)
    return actors


def series_id_directores_get(id):  # noqa: E501
    """Obtener los directores de una serie específica

     # noqa: E501

    :param id: ID de la serie
    :type id: str

    :rtype: List[Director]
    """
    return 'No hay directores para las series'


def series_id_get(id):  # noqa: E501
    """Obtener una serie por ID

     # noqa: E501

    :param id: ID de la serie a buscar
    :type id: str

    :rtype: Serie
    """
    info = db.dbGetSerieById(id)
    serie = Serie(info[0], info[1], info[2], info[3], series_id_actores_get(info[0]), temporadas_controller.series_id_temporadas_get(info[0]))
    return serie.to_dict()


def series_titulo_titulo_get(titulo):  # noqa: E501
    """Obtener una serie por Nombre

     # noqa: E501

    :param titulo: Serie con el nombre a buscar
    :type titulo: str

    :rtype: List[Serie]
    """
    series = []
    for info in db.dbGetSeriesByTitle(titulo):
        serie = Serie(info[0], info[1], info[2], info[3], series_id_actores_get(info[0]), temporadas_controller.series_id_temporadas_get(info[0]))
        series.append(serie.to_dict())
    return series