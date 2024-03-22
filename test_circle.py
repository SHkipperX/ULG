import unittest

from geometry import Circle

__all__ = []


class TestCircle(unittest.TestCase):
    def test_uncreate_m(self):
        with self.assertRaises(ValueError) as context:
            Circle(-1)

        self.assertIsInstance(context.exception, ValueError)

    def test_uncreate_l(self):
        with self.assertRaises(TypeError) as context:
            Circle("1")

        self.assertIsInstance(context.exception, TypeError)

    def test_create_c(self):
        c = Circle(1)
        area = c.get_area
        self.assertGreater(area, 3)


if __name__ == "__main__":
    unittest.main()
    "1"