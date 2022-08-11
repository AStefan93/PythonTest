""" Hello world tests """
import unittest
from .hello_world import output_hello_world


class TestHelloWorld(unittest.TestCase):
    """Hello world tests"""

    def test_print_hello_world(self):
        """This test test the function prints hello world"""
        self.assertEqual(output_hello_world(), "hello world\n")


if __name__ == "__main__":
    unittest.main()
