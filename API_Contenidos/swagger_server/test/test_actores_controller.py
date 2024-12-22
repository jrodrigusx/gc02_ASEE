# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.actor import Actor  # noqa: E501
from ..test import BaseTestCase


class TestActoresController(BaseTestCase):
    """ActoresController integration test stubs"""

    def test_actores_get(self):
        """Test case for actores_get

        Obtener todos los actores
        """
        response = self.client.open(
            '/actores',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_actores_id_get(self):
        """Test case for actores_id_get

        Obtener actor por id
        """
        response = self.client.open(
            '/actores/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
