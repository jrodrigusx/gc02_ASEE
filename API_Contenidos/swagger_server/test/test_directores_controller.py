# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.director import Director  # noqa: E501
from ..test import BaseTestCase


class TestDirectoresController(BaseTestCase):
    """DirectoresController integration test stubs"""

    def test_directores_get(self):
        """Test case for directores_get

        Obtener todos los directores
        """
        response = self.client.open(
            '/directores',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_directores_id_get(self):
        """Test case for directores_id_get

        Obtener director por id
        """
        response = self.client.open(
            '/directores/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
