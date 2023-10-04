# Exercise 2: Write a function that accepts a string and returns the longest palindromic substring in that string.

def longest_palindromic_substring(s):
    if not s:
        return ""

    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]
# Unit tests
import unittest

class TestExercise2(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")

if __name__ == '__main__':
    unittest.main()
