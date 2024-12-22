# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.visualizaciones_peliculas import VisualizacionesPeliculas  # noqa: E501
from ..test import BaseTestCase


class TestVisualizacionesPeliculasController(BaseTestCase):
    """VisualizacionesPeliculasController integration test stubs"""

    def test_visualizaciones_peliculas_id_get(self):
        """Test case for visualizaciones_peliculas_id_get

        las visualizaciones de una pelicula
        """
        response = self.client.open(
            '/visualizacionesPeliculas/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_visualizaciones_peliculas_id_put(self):
        """Test case for visualizaciones_peliculas_id_put

        Actualizar las visualizaciones de una película
        """
        body = VisualizacionesPeliculas()
        response = self.client.open(
            '/visualizacionesPeliculas/{id}/update'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
