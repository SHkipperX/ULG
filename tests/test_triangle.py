import unittest
import setup

from geometry import Triangle

__all__ = []


class TestTriangle(unittest.TestCase):
    def test_uncreate_vle(self):
        with self.assertRaises(ValueError):
            Triangle(1, -1, 1)

    def test_uncreate_tpe(self):
        with self.assertRaises(TypeError):
            Triangle("1", 2, 4)

    def test_create_tgl(self):
        trg = Triangle(1, 2, 2.8)
        area = trg.get_area
        self.assertLess(area, 0.71)
        type_trg = trg.get_type_triangle
        self.assertEqual(type_trg, "obtuse angled")
        with self.assertRaises(AttributeError):
            trg.__hipotenusa


if __name__ == "__main__":
    unittest.main()
