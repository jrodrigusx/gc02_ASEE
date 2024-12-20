import connexion
import six

from ..models.director import Director  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_contenidos as db

def directores_get():  # noqa: E501
    """Obtener todos los directores

     # noqa: E501


    :rtype: List[Director]
    """
    directors = []
    for info in db.dbGetDirectors():
        director = Director(info[0], info[1], info[2])
        directors.append(director.to_dict())
    return directors


def directores_id_get(id):  # noqa: E501
    """Obtener director por id

     # noqa: E501

    :param id: Director por ID
    :type id: str

    :rtype: Director
    """
    info = db.dbGetDirectorById(id)
    director = Director(info[0], info[1], info[2])
    return director.to_dict()
