import unittest

from fnplus.either import Either


class TestEither(unittest.TestCase):

    def test_init(self):
        either = Either(1, None)
        self.assertEqual(1, either.get_value())
        self.assertIsNone(either.get_error())

        error_either = Either(None, Exception("Foo"))
        self.assertIsNone(error_either.get_value())
        self.assertEqual("Foo", error_either.get_error().args[0])

    def test_error_type(self):
        self.assertEqual(Exception, Either(None, Exception()).error_type())
        self.assertEqual(KeyError, Either(None, KeyError()).error_type())
        self.assertEqual(type(None), Either(1, None).error_type())

    def test_try(self):
        either = Either.try_(lambda x: x)(2)
        self.assertEqual(2, either.get_value())
        self.assertIsNone(either.get_error())

    def test_try_with_error(self):
        def _raiser(): raise Exception("Foo")
        either = Either.try_(_raiser)()
        self.assertIsNone(either.get_value())
        self.assertEqual("Foo", either.get_error().args[0])

    def test_try_with_derived_error(self):
        def _raiser(): raise KeyError("Foo")
        either = Either.try_(_raiser)()
        self.assertIsNone(either.get_value())
        self.assertEqual("Foo", either.get_error().args[0])

    def test_bind(self):
        either = Either.bind(lambda x: x + 1)(Either(1))
        self.assertEqual(2, either.get_value())
        self.assertIsNone(either.get_error())

        error_either = Either.bind(lambda x: x + 1)(Either(None, Exception("Foo")))
        self.assertIsNone(error_either.get_value())
        self.assertEqual("Foo", error_either.get_error().args[0])

    def test_try_bind(self):
        bound_inc = Either.try_bind(lambda x: x+1)
        self.assertEqual(4, bound_inc(Either(3)).get_value())
        self.assertIsNone(bound_inc(Either(None, Exception())).get_value())

    def test_try_bind_with_error(self):
        def _raiser(): raise Exception("Foo")
        bound_either = Either.try_bind(_raiser)(Either(None, Exception("Bar")))

        self.assertIsNone(bound_either.get_value())
        self.assertEqual("Bar", bound_either.get_error().args[0])
