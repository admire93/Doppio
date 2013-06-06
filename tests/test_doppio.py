import unittest
import doppio

class DoppioTestCase(unittest.TestCase):
    def setUp(self):
        token = '16438f80e29d-e7bc-4c90-8f01-040636acabbd::1643'
        self.doppio = doppio.Doppio(token)

    def test_uri_make(self):
        self.assertEqual(self.doppio.route('point'), 'http://api.mintpresso.com:80/v1/account/1643/point?api_token=16438f80e29d-e7bc-4c90-8f01-040636acabbd', 'URI test')
        self.assertEqual(self.doppio.route('point.id', 1), 'http://api.mintpresso.com:80/v1/account/1643/point/1?api_token=16438f80e29d-e7bc-4c90-8f01-040636acabbd', 'URI test for point.id')
        self.assertEqual(self.doppio.route('edge'), 'http://api.mintpresso.com:80/v1/account/1643/edge?api_token=16438f80e29d-e7bc-4c90-8f01-040636acabbd', 'URI test for edge')

    def test_set(self):
        res = self.doppio.set(type='testtype', identifier='admire93@somemail.com')
        self.assertTrue(res.has_key(u'point'), 'Doppio.set(type=,identifier=) has key `point`.')
        self.assertEqual(res[u'point'][u'type'], u'testtype', 'Doppio.set(type=,identifier=) return right value.')
