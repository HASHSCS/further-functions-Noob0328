# Exercise 2: Write a function that accepts a string and returns the longest palindromic substring in that string.

def longest_palindromic_substring(s):
    # Your code here
    pass

# Unit tests
import unittest

class TestExercise2(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")

if __name__ == '__main__':
    unittest.main()
