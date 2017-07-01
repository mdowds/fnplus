import unittest

from fnplus.curried import curried


class TestCurried(unittest.TestCase):

    def test_curried(self):

        @curried
        def f(a, b, c):
            return a + b + c

        self.assertEqual(6, f(1,2)(3))
        self.assertEqual(6, f(1,2,3))
