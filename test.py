from addition import *
import unittest

class test_addition(unittest.TestCase):

    def test_addition(self):
        self.assertEquals(addition(3,7) == 10)
