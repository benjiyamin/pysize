
import unittest

import numpy
from numpy import testing

from pysize import category, convert, options, base


class ConversionTest(unittest.TestCase):

    def test_invalid_from_parameter(self):
        with self.assertRaises(ValueError):
            category('fdsfhjkwbf')

    def test_base_unit_detection(self):
        produced = base('mm')
        expected = 'm'
        self.assertEqual(produced, expected)

    def test_options(self):
        produced = options('mm')
        included = 'm'
        self.assertIn(included, produced)

    def test_convert_from_base(self):
        produced = convert(1.0).frm('m').to('mm')
        expected = 1000.0
        self.assertEqual(produced, expected)

    def test_convert_to_base(self):
        produced = convert(1000.0).frm('mm').to('m')
        expected = 1.0
        self.assertEqual(produced, expected)

    def test_convert_to_base_and_back(self):
        a = 1000.0
        b = convert(a).frm('mm').to('m')
        produced = convert(b).frm('m').to('mm')
        expected = a
        self.assertEqual(produced, expected)

    def test_numpy_array_conversion(self):
        a = numpy.array([[1.0, 2.0], [3.0, 4.0]])
        produced = convert(a).frm('m').to('mm')
        expected = numpy.array([[1000.0, 2000.0], [3000.0, 4000.0]])
        testing.assert_array_equal(produced, expected)
