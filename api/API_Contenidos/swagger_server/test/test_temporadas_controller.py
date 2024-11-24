# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.temporada import Temporada  # noqa: E501
from ..test import BaseTestCase


class TestTemporadasController(BaseTestCase):
    """TemporadasController integration test stubs"""

    def test_series_id_temporadas_get(self):
        """Test case for series_id_temporadas_get

        Obtener todas las temporadas de una serie
        """
        response = self.client.open(
            '/series/{id}/temporadas'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
