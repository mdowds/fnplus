import unittest

from fnplus.iterable import *


class TestIterable(unittest.TestCase):

    def test_tmap(self):
        self.assertEqual((2,3,4), tmap(lambda x: x + 1, (1, 2, 3)))
        self.assertEqual((2,3,4), tmap(lambda x: x + 1, [1, 2, 3]))

    def test_tfilter(self):
        self.assertEqual((1,2), tfilter(lambda x: x < 10, (1, 2, 11, 12)))
        self.assertEqual((1,2), tfilter(lambda x: x < 10, [1, 2, 11, 12]))

    def test_find(self):
        self.assertEqual("foo", find(lambda x: x == "foo", ("foo", "bar")))
        self.assertEqual("foo", find(lambda x: x == "foo", ["foo", "bar"]))
