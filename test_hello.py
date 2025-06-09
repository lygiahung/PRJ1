import unittest
from hello import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("lygiahung"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()