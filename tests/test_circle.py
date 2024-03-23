import unittest
import setup

from geometry import Circle

__all__ = []


class TestCircle(unittest.TestCase):
    def test_uncreate_vle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_uncreate_tpe(self):
        with self.assertRaises(TypeError):
            Circle("1")

    def test_create_success(self):
        circle = Circle(1)
        area = circle.get_area
        self.assertGreater(area, 3)
        with self.assertRaises(AttributeError):
            circle.__radius


if __name__ == "__main__":
    unittest.main()
