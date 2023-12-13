from unittest import TestCase, main
from array import monotton_array


class Testarray(TestCase):
    def test_array_up(self):
        self.assertEqual(monotton_array([1, 2, 3, 4, 5]), True)
    def test_array_down(self):
        self.assertEqual(monotton_array([5, 4, 3, 2, 1]), True)
    def test_array_false(self):
        self.assertEqual(monotton_array([1, 2, 2, 3, 2, 4]), False)
    def test_array_minus(self):
        self.assertEqual(monotton_array([2,2,-1]),True)
    def test_array_equal(self):
        self.assertEqual(monotton_array([2,2,2,2]),True)
    def test_array_last(self):
        self.assertEqual(monotton_array([2,2,2,3]),True)
    def test_array_one(self):
        self.assertEqual(monotton_array([3]),True)
    def test_array_null(self):
        self.assertEqual(monotton_array([]), False)
