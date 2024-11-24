# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from ..models.visualizaciones_series import VisualizacionesSeries  # noqa: E501
from ..test import BaseTestCase


class TestVisualizacionesSeriesController(BaseTestCase):
    """VisualizacionesSeriesController integration test stubs"""

    def test_visualizaciones_series_id_get(self):
        """Test case for visualizaciones_series_id_get

        Obtener las visualizaciones de una Serie
        """
        response = self.client.open(
            '/visualizacionesSeries/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_visualizaciones_series_id_put(self):
        """Test case for visualizaciones_series_id_put

        Actualizar las visualizaciones de una serie
        """
        body = VisualizacionesSeries()
        response = self.client.open(
            '/visualizacionesSeries/{id}/update'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
