import unittest
import name

class TestCase(unittest.TestCase):
    def test_name1(self):
        self.assertEqual(name.printName("Luna", "Bretl"), "Luna Bretl")
    def test_name2(self):
        self.assertEqual(name.printName("Hello", "World"), "Hello World")
    def test_name3(self):
        self.assertEqual(name.printName(1, 2), "1 2")


if __name__ == '__main__':
    unittest.main()