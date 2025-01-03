# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from .. import util


class IdGenerofavoritoBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, genero_favorito: str=None):  # noqa: E501
        """IdGenerofavoritoBody - a model defined in Swagger

        :param genero_favorito: The genero_favorito of this IdGenerofavoritoBody.  # noqa: E501
        :type genero_favorito: str
        """
        self.swagger_types = {
            'genero_favorito': str
        }

        self.attribute_map = {
            'genero_favorito': 'genero_favorito'
        }
        self._genero_favorito = genero_favorito

    @classmethod
    def from_dict(cls, dikt) -> 'IdGenerofavoritoBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The id_generofavorito_body of this IdGenerofavoritoBody.  # noqa: E501
        :rtype: IdGenerofavoritoBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def genero_favorito(self) -> str:
        """Gets the genero_favorito of this IdGenerofavoritoBody.

        Nuevo género favorito  # noqa: E501

        :return: The genero_favorito of this IdGenerofavoritoBody.
        :rtype: str
        """
        return self._genero_favorito

    @genero_favorito.setter
    def genero_favorito(self, genero_favorito: str):
        """Sets the genero_favorito of this IdGenerofavoritoBody.

        Nuevo género favorito  # noqa: E501

        :param genero_favorito: The genero_favorito of this IdGenerofavoritoBody.
        :type genero_favorito: str
        """

        self._genero_favorito = genero_favorito
