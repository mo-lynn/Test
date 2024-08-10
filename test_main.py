import unittest
from main import is_even

class TestMain(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

if __name__ == "__main__":
    unittest.main()
