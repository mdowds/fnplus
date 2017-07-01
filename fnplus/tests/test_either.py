import unittest

from fnplus.either import Either


class TestEither(unittest.TestCase):

    def test_init(self):
        either = Either(1, None)
        self.assertEqual(1, either.get_value())
        self.assertIsNone(either.get_error())

        error_either = Either(None, Exception("Foo"))
        self.assertIsNone(error_either.get_value())
        self.assertEqual("Foo", error_either._error.args[0])

    def test_try(self):
        either = Either.try_(lambda x: x)(2)
        self.assertEqual(2, either.get_value())
        self.assertIsNone(either.get_error())

    def test_try_with_error(self):
        def _raiser(): raise Exception("Foo")
        either = Either.try_(_raiser)()
        self.assertIsNone(either.get_value())
        self.assertEqual("Foo", either._error.args[0])

    def test_try_with_derived_error(self):
        def _raiser(): raise KeyError("Foo")
        either = Either.try_(_raiser)()
        self.assertIsNone(either.get_value())
        self.assertEqual("Foo", either._error.args[0])

    def test_bind(self):
        self.assertEqual(2, Either(1)._bind(lambda x: x + 1).get_value())
        self.assertEqual("Foo", Either(None, Exception("Foo"))._bind(lambda x: x + 1)._error.args[0])

    # def test_try_bind(self):
    #     bound_inc = Either.try_bind(lambda x: x+1)
    #     self.assertEqual(4, bound_inc(Either(3))._value)
    #     self.assertIsNone(bound_inc(Either(None, Exception()))._value)
