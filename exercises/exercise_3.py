# Exercise 3: Write a function to find the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    # Your code here
    pass

# Unit tests
import unittest

class TestExercise3(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(56, 98), 14)
        self.assertEqual(gcd(54, 24), 6)

if __name__ == '__main__':
    unittest.main()
