import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))
        
if __name__ == '__main__':
    unittest.main()