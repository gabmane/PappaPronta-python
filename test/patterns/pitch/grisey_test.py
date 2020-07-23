import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import PappaPronta
from PappaPronta.patterns.pitch.grisey import Grisey
from PappaPronta.patterns.pitch.sieve import sieve

class TestPatternClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 10
        self.base_f = 0.18
        self.sp    = 1000
        self.op    = 2000
        self.c     = Grisey(self.start, self.dur, self.base_f, self.sp, self.op)

    def test_creation(self):
        self.assertTrue(self.c)

    def test_next(self):
        vshb = sieve(self.sp, self.op)
        vals_should_be = [float(self.base_f)*p for p in vshb]
        t = self.c.at
        sz = len(self.c.values)
        idx = 0
        while (idx < sz):
            y_should_be = vals_should_be[idx]
            idx += 1
            y_is = self.c.next(t)
            self.assertEqual(y_is, y_should_be)

if __name__ == '__main__':
    unittest.main()
