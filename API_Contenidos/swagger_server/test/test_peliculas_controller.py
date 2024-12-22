# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.actor import Actor  # noqa: E501
from ..models.director import Director  # noqa: E501
from ..models.pelicula import Pelicula  # noqa: E501
from ..test import BaseTestCase


class TestPeliculasController(BaseTestCase):
    """PeliculasController integration test stubs"""

    def test_peliculas_genero_genero_get(self):
        """Test case for peliculas_genero_genero_get

        Obtener todas las películas
        """
        response = self.client.open(
            '/peliculas/genero/{genero}'.format(genero='genero_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_peliculas_get(self):
        """Test case for peliculas_get

        Obtener todas las películas
        """
        response = self.client.open(
            '/peliculas',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_peliculas_id_actores_get(self):
        """Test case for peliculas_id_actores_get

        Obtener los actores de una película específica
        """
        response = self.client.open(
            '/peliculas/{id}/actores'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_peliculas_id_directores_get(self):
        """Test case for peliculas_id_directores_get

        Obtener los directores de una película específica
        """
        response = self.client.open(
            '/peliculas/{id}/directores'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_peliculas_id_get(self):
        """Test case for peliculas_id_get

        Obtener una pelicula por id
        """
        response = self.client.open(
            '/peliculas/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_peliculas_titulo_titulo_get(self):
        """Test case for peliculas_titulo_titulo_get

        Obtener todas las películas que contengan el título
        """
        response = self.client.open(
            '/peliculas/titulo/{titulo}'.format(titulo='titulo_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
