# Exercise 2: Write a function that accepts a string and returns the longest palindromic substring in that string.
def longest_palindromic_substring(s):
    if len(s) <= 1:
        return s 
    longest_palindrome = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(s, i, i)
        even_palindrome = expand_around_center(s, i, i + 1)
        palindrome = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome
        
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome

    return longest_palindrome

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]
    
# Unit tests
import unittest

class TestExercise2(unittest.TestCase):

    def test_longest_palindromic_substring(self):
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")

if __name__ == '__main__':
    unittest.main()
