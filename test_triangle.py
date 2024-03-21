import unittest

from geometry import Triangle

__all__ = []

class TestTriangle(unittest.TestCase):
    def test_uncreate_m(self):
        with self.assertRaises(ValueError) as context:
            Triangle(1, 1, 1, 1)
        
        self.assertIsInstance(context.exception, ValueError)

        with self.assertRaises(ValueError) as context:
            Triangle(1, -1, 1)
        
        self.assertIsInstance(context.exception, ValueError)
    
    def test_uncreate_l(self):
        with self.assertRaises(TypeError) as context:
            Triangle("1", 2, 4)
        
        self.assertIsInstance(context.exception, TypeError)

    def test_create_tgl(self):
        t = Triangle(1, 2, 2.8)
        area = t.get_area
        self.assertLess(area, 0.71)
        type_ = t.get_type_triangle
        self.assertEqual(type_, "obtuse angled")

if __name__ == "__main__":
    unittest.main()