
import unittest

from pysize import convert


class FactoredTest(unittest.TestCase):

    def test_velocity_conversion(self):
        produced = convert(60.0).frm('mi/h').to('ft/s')
        expected = 88.0
        self.assertEqual(produced, expected)

    def test_volume_conversion(self):
        produced = convert(1.0).frm('yd^3').to('ft^3')
        expected = 27.0
        self.assertEqual(produced, expected)
