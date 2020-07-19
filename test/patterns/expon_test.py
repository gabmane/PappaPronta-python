import sys
import os
import unittest
from math import log, exp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PappaPronta
from PappaPronta.patterns.expon import Expon

class TestPatternClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 10
        self.svalue = 10.0
        self.evalue = 20.0
        self.e     = Expon(self.start, self.dur, self.svalue, self.evalue)

    def test_creation(self):
        self.assertTrue(self.e)

    def test_properties(self):
        self.assertEqual(self.e.at, self.start)
        self.assertEqual(self.e.dur, self.dur)
        self.assertEqual(self.e.start_value, self.svalue)
        self.assertEqual(self.e.end_value, self.evalue)

    def test_next(self):
        afact = (log(self.evalue)-log(self.svalue))/self.dur
        bfact = log(self.svalue) - (afact * self.start)
        t = self.e.at
        step = 0.1
        while (t < self.e.end()):
            y_should_be = exp(afact * t + bfact)
            y_is = self.e.next(t)
            self.assertEqual(y_is, y_should_be)
            t += step

if __name__ == '__main__':
    unittest.main()
