import connexion
import six

from ..models.actor import Actor  # noqa: E501
from .. import util

from flask import request, jsonify
from ..... import dbconnection

def actores_get():  # noqa: E501
    """Obtener todos los actores

     # noqa: E501


    :rtype: List[Actor]
    """
    return dbconnection.dbGetActors()


def actores_id_get(id):  # noqa: E501
    """Obtener actor por id

     # noqa: E501

    :param id: Actor Correspondiente a ese id
    :type id: str

    :rtype: Actor
    """
    return dbconnection.dbGetActor(id)

