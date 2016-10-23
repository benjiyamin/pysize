
import unittest

from pysize import parse


class ParseTest(unittest.TestCase):

    def test_parse_divide(self):
        produced = parse('m/s')
        expected = ['m'], ['s']
        self.assertEqual(produced, expected)

    def test_parse_multiply(self):
        produced = parse('m-s')
        expected = ['m', 's'], []
        self.assertEqual(produced, expected)

    def test_parse_exponent(self):
        produced = parse('ft^3')
        expected = ['ft', 'ft', 'ft'], []
        self.assertEqual(produced, expected)

    def test_multiple_divide_and_exponent(self):
        produced = parse('kg-m/s^2')
        expected = ['kg', 'm'], ['s', 's']
        self.assertEqual(produced, expected)
