from unittest import TestCase, main
from bilboard import bilboard

class Testarray(TestCase):
    def test_case1(self):
        arr = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        result = bilboard(10, 5, arr)
        self.assertEqual(result, 100)

    def test_case2(self):
        arr = [5, 10, 15, 20, 25,10 ,20, 5, 10]
        result = bilboard(3, 2, arr)
        self.assertEqual(result, 110)

    def test_case3(self):
        arr = [5, 5, 5, 5, 5, 5, 5, 5]
        result = bilboard(4, 1, arr)
        self.assertEqual(result, 10)

    def test_case4(self):
        arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        result = bilboard(5, 3, arr)
        self.assertEqual(result, 570)
    def test_case5(self):
        arr = [1]*100
        arr[99] = 30
        result = bilboard(10, 2, arr)
        self.assertEqual(result, 78)
