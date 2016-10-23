
import unittest

from pysize import category
from pysize import registry


class DistanceConversionTest(unittest.TestCase):

    def test_category_detection(self):
        produced = category('m')
        expected = registry.base['distance']
        self.assertEqual(produced, expected)
