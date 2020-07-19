import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PappaPronta
from PappaPronta.patterns.linear import Linear

class TestPatternClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 10
        self.svalue = -10.0
        self.evalue = 10.0
        self.l     = Linear(self.start, self.dur, self.svalue, self.evalue)

    def test_creation(self):
        self.assertTrue(self.l)

    def test_properties(self):
        self.assertEqual(self.l.at, self.start)
        self.assertEqual(self.l.dur, self.dur)
        self.assertEqual(self.l.start_value, self.svalue)
        self.assertEqual(self.l.end_value, self.evalue)

    def test_next(self):
        afact = (self.evalue-self.svalue)/self.dur
        bfact = self.svalue - (afact * self.start)
        t = self.l.at
        step = 0.1
        while (t < self.l.end()):
            y_should_be = afact * t + bfact
            self.assertEqual(self.l.next(t), y_should_be)
            t += step

if __name__ == '__main__':
    unittest.main()

