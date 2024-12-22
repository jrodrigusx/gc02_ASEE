# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.recomendaciones_peliculas import RecomendacionesPeliculas  # noqa: E501
from ..test import BaseTestCase


class TestRecomendacionesPeliculasController(BaseTestCase):
    """RecomendacionesPeliculasController integration test stubs"""

    def test_recomendaciones_peliculas_id_get(self):
        """Test case for recomendaciones_peliculas_id_get

        Obtener las recomendaciones para un usario de películas
        """
        response = self.client.open(
            '/recomendacionesPeliculas/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recomendaciones_peliculas_id_put(self):
        """Test case for recomendaciones_peliculas_id_put

        Actualizar las recomendaciones de películas
        """
        body = RecomendacionesPeliculas()
        response = self.client.open(
            '/recomendacionesPeliculas/{id}/update'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
