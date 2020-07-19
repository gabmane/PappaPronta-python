import sys
import os
import unittest
from math import log, exp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PappaPronta
from PappaPronta.patterns.sequence import Sequence

class TestPatternClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 10
        self.values = [3, 4, 5.5]
        self.s     = Sequence(self.start, self.dur, self.values)

    def test_creation(self):
        self.assertTrue(self.s)

    def test_properties(self):
        self.assertEqual(self.s.at, self.start)
        self.assertEqual(self.s.dur, self.dur)
        self.assertEqual(self.s.values, self.values)

    def test_next(self):
        t = self.s.at
        step = 0.1
        sz = len(self.values)
        idx = 0
        while (t < self.s.end()):
            y_should_be = self.values[idx]
            idx += 1
            if (idx >= sz):
                idx = 0
            y_is = self.s.next(t)
            self.assertEqual(y_is, y_should_be)
            t += step

    def test_next_exception(self):
        self.assertRaises(self.s.next(self.s.end()*2))

if __name__ == '__main__':
    unittest.main()

