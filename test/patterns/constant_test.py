import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PappaPronta
from PappaPronta.patterns.constant import Constant

class TestPatternClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 1
        self.value = 3.14
        self.c     = Constant(self.start, self.dur, self.value)

    def test_creation(self):
        self.assertTrue(self.c)

    def test_properties(self):
        self.assertEqual(self.c.at, self.start)
        self.assertEqual(self.c.dur, self.dur)
        self.assertEqual(self.c.value, self.value)

    def test_next(self):
        for t in range(int(self.start*10), int((self.start + self.dur) * 10)):
            self.assertTrue(self.c.next(t/10))

if __name__ == '__main__':
    unittest.main()
