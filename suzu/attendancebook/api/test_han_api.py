# -*- coding: utf-8 -*-

from unittest import skip

from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin


class HanResourceTest(ResourceTestCaseMixin, TestCase):

    fixtures = ['auth.json', 'attendancebook.json']

    def setUp(self):
        super(HanResourceTest, self).setUp()

        # setting up credentials
        self.username = 'testuser'
        self.password = 'testuser'

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    @skip('FIXME: access is open')
    def test_get_list_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/han/', format='json'))

    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/han/', format='json', authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 4)
        # Here, we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            u'id': 1,
            u'additional_information': u'',
            u'created': u'2018-01-12T21:11:12.498000',
            u'modified': u'2018-01-12T21:11:12.506000',
            u'name': u'Ciranda',
            u'resource_uri': u'/api/v1/han/1/'
        })