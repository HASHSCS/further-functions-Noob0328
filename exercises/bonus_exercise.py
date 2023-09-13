# Bonus Exercise: Create a function that converts a number to its Roman numeral representation.

def to_roman(num):
    # Your code here
    pass

# Unit tests
import unittest

class TestBonusExercise(unittest.TestCase):

    def test_to_roman(self):
        self.assertEqual(to_roman(58), "LVIII")
        self.assertEqual(to_roman(1994), "MCMXCIV")

if __name__ == '__main__':
    unittest.main()
