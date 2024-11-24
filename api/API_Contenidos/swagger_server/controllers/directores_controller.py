import connexion
import six

from ..models.director import Director  # noqa: E501
from .. import util

from flask import request, jsonify
from ..... import dbconnection

def directores_get():  # noqa: E501
    """Obtener todos los directores

     # noqa: E501


    :rtype: List[Director]
    """
    return dbconnection.dbGetDirectors()


def directores_id_get(id):  # noqa: E501
    """Obtener director por id

     # noqa: E501

    :param id: Director por ID
    :type id: str

    :rtype: Director
    """
    return dbconnection.dbGetDirectorById(id)
