import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PappaPronta
from PappaPronta.patterns.pattern import Pattern

class TestPatternClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 1
        self.p     = Pattern(self.start, self.dur)
        self.good_t= self.start + (self.dur/2)
        self.bad_t = self.start + (self.dur*2)

    def test_creation(self):
        self.assertTrue(self.p)

    def test_properties(self):
        self.assertEqual(self.p.at, self.start)
        self.assertEqual(self.p.dur, self.dur)

    def test_check_time(self):
        self.assertTrue(self.p.check_time(self.good_t))
        self.assertFalse(self.p.check_time(self.bad_t))

    def test_end(self):
        self.assertEqual(self.p.end(), self.start+self.dur)

    def test_next(self):
        self.assertFalse(self.p.next(self.good_t))

    def test_next_exception(self):
        self.assertRaises(self.p.next(self.bad_t))

if __name__ == '__main__':
    unittest.main()
