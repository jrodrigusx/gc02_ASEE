import connexion
import six

from ..models.actor import Actor  # noqa: E501
from .. import util

from flask import request, jsonify
from ... import dbconnection_contenidos as db

def actores_get():  # noqa: E501
    """Obtener todos los actores

     # noqa: E501


    :rtype: List[Actor]
    """
    actors = []
    for info in db.dbGetActors():
        actor = Actor(info[0], info[1], info[2])
        actors.append(actor.to_dict())
    return actors

def actores_id_get(id):  # noqa: E501
    """Obtener actor por id

     # noqa: E501

    :param id: Actor Correspondiente a ese id
    :type id: str

    :rtype: Actor
    """
    info = db.dbGetActor(id)
    actor = Actor(info[0], info[1], info[2])
    return actor.to_dict()