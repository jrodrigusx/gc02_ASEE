# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.actor import Actor  # noqa: E501
from ..models.director import Director  # noqa: E501
from ..models.serie import Serie  # noqa: E501
from ..test import BaseTestCase


class TestSeriesController(BaseTestCase):
    """SeriesController integration test stubs"""

    def test_series_genero_genero_get(self):
        """Test case for series_genero_genero_get

        Obtener una serie por genero
        """
        response = self.client.open(
            '/series/genero/{genero}'.format(genero='genero_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_series_get(self):
        """Test case for series_get

        Obtener todas las series
        """
        response = self.client.open(
            '/series',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_series_id_actores_get(self):
        """Test case for series_id_actores_get

        Obtener actores de una serie específica
        """
        response = self.client.open(
            '/series/{id}/actores'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_series_id_directores_get(self):
        """Test case for series_id_directores_get

        Obtener los directores de una serie específica
        """
        response = self.client.open(
            '/series/{id}/directores'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_series_id_get(self):
        """Test case for series_id_get

        Obtener una serie por ID
        """
        response = self.client.open(
            '/series/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_series_titulo_titulo_get(self):
        """Test case for series_titulo_titulo_get

        Obtener una serie por Nombre
        """
        response = self.client.open(
            '/series/titulo/{titulo}'.format(titulo='titulo_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
