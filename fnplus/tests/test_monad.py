import unittest

from fnplus.monad import Monad
from fnplus.either import Either


class FunctionalTests(unittest.TestCase):

    def test_call_partial_with_Either(self):
        bound_inc = Monad.call_partial(lambda x: x + 1)
        self.assertEqual(4, bound_inc(Either(3))._value)
        self.assertIsNone(bound_inc(Either(None, Exception()))._value)
