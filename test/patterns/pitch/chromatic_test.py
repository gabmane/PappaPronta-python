import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import PappaPronta
from PappaPronta.patterns.pitch.chromatic import Chromatic

class TestPatternClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 10
        self.startfrq = 65.6
        self.nnotes = 200
        self.ob     = 3        # octave base
        self.npo    = 13       # notes per octave
        self.c     = Chromatic(self.start, self.dur, self.startfrq, self.nnotes, self.ob, self.npo)

    def test_creation(self):
        self.assertTrue(self.c)

    def test_properties(self):
        self.assertEqual(len(self.c.values), self.nnotes)

    def test_next(self):
        vals_should_be = [(float(self.startfrq)*(float(self.ob)**(x/float(self.npo)))) for x in range(self.nnotes)]
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
