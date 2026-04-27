import unittest
from chiffrement import Logique

class CaesarTest(unittest.TestCase):
    def upper_test(self):
        self.assertEqual(Logique("ABC",3), "DEF")
    def lower_test(self):
        self.assertEqual(Logique("abc",3), "def")
    def empaty_test(self):
        self.assertEqual(Logique(" ", 3), " ")

if __name__ =="__main__":
    unittest.main()