# Exercise 1: Create a function that calculates the area of different shapes. 
# The function should take the shape type and its parameters as inputs.
import math 
def calculate_area(shape, *args):
    if shape=="square":
        side=args[0]
        return side**2
    elif shape=="rectangle":
        length=args[0]
        width=args[1]
        return length * width
    elif shape=="triangle":
        base=args[0]
        height=args[1]
        return base*height/2
    elif shape == "circle":
        radius = args[0]
        return math.pi * (radius ** 2)
   

# Unit tests
import unittest

class TestExercise1(unittest.TestCase):

    def test_calculate_area(self):
        self.assertEqual(calculate_area("square", 4), 16)
        self.assertEqual(calculate_area("rectangle", 4, 7), 28)
        self.assertEqual(calculate_area("triangle", 3, 6), 9)
        self.assertEqual(calculate_area("circle", 3), 28.27)

if __name__ == '__main__':
    unittest.main()
