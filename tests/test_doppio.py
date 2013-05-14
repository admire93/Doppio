import unittest
import doppio

class DoppioTestCase(unittest.TestCase):
    def setUp(self):
        token = "16438f80e29d-e7bc-4c90-8f01-040636acabbd::1643"
        self.doppio = doppio.Doppio(token)

    def test_set(self):
        self.assertEqual() 
        res = doppio.set(type="test", identifier=1)
        self.assertEqual(res, {"type": "test", "identifier": "1"}, "Doppio.set(type=,identifier=)")
