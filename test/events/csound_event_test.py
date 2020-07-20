import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PappaPronta
from PappaPronta.events.csound_event import CsoundEvent

class TestCsoundEventClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 1
        self.parms = [4, 5, 6, 7, 8]
        self.instrno = 1
        self.ce    = CsoundEvent(self.start, self.dur, self.instrno, self.parms)
        self.output = 'i001   0.0000   1.0000   4.0000   5.0000   6.0000   7.0000   8.0000 '

    def test_creation(self):
        self.assertTrue(self.ce)

    def test_properties(self):
        self.assertEqual(self.ce.at, self.start)
        self.assertEqual(self.ce.dur, self.dur)
        self.assertEqual(self.ce.parameters, self.parms)

    def test_output(self):
        self.assertEqual(self.ce.output(), self.output)

if __name__ == '__main__':
    unittest.main()

