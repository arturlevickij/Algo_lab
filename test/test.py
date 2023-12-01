from unittest import TestCase, main
from main import find_text

class TestFindText(TestCase):
    def test_find1(self):
        haystack = "text"
        needle ="sone text in text"
        result = find_text(haystack, needle)
        self.assertEqual(result, [5, 13])

    def test_find2(self):
        haystack = "abc"
        needle = "aabcabc"
        result = find_text(haystack, needle)
        self.assertEqual(result, [1, 4])

    def test_find3(self):
        haystack = "abc"
        needle = "bcdabc"
        result = find_text(haystack, needle)
        self.assertEqual(result, [3])

    def test_find4(self):
        haystack = "xyz"
        needle = "abcdefgh"
        result = find_text(haystack, needle)
        self.assertEqual(result, [])

    def test_find5(self):
        haystack = "abcd"
        needle = "aabcdabc"
        result = find_text(haystack, needle)
        self.assertEqual(result, [1])

    def test_find6(self):
        haystack = "ac"
        needle = "bacdefg"
        result = find_text(haystack, needle)
        self.assertEqual(result, [1])