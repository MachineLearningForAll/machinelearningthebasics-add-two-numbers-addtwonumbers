import unittest
from student.add import add

class TestAddVisible(unittest.TestCase):
    def test_add_small(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
