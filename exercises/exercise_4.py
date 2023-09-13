# Exercise 4: Create a function to check whether the brackets in a given string are balanced or not.

def are_brackets_balanced(s):
    # Your code here
    pass

# Unit tests
import unittest

class TestExercise4(unittest.TestCase):

    def test_are_brackets_balanced(self):
        self.assertTrue(are_brackets_balanced("({[]})"))
        self.assertFalse(are_brackets_balanced("([)]"))
        self.assertFalse(are_brackets_balanced("{[}"))

if __name__ == '__main__':
    unittest.main()
