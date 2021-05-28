# The code is written as driver code. Can you convert it to Unit Test?

import unittest
from armstrong_numbers import find_armstrong_numbers

class ArmstrongNumbersTestCase(unittest.TestCase):

    def test_returns_a_list(self):
        """When you call find_armstrong_numbers, it should return an array/list."""
        self.assertEqual(type(find_armstrong_numbers(list(range(0,8)))), list)

    def test_returns_the_correct_list(self):
        """When you call: find_armstrong_numbers(list)"""
        self.assertEqual(type(find_armstrong_numbers(list(range(0,8)))), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(type(find_armstrong_numbers(list(range(0,100)))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(type(find_armstrong_numbers(list(range(0,999)))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()

# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
