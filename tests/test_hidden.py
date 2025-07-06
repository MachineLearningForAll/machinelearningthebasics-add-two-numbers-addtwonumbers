import unittest
from student.add import add

class TestAddHidden(unittest.TestCase):
    def test_large_numbers(self):
        self.assertEqual(add(1000000, 999999), 1999999)

    def test_negative_numbers(self):
        self.assertEqual(add(-5, -7), -12)

if __name__ == '__main__':
    unittest.main()
