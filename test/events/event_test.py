import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PappaPronta
from PappaPronta.events.event import Event

class TestEventClass(unittest.TestCase):

    def setUp(self):
        self.start = 0
        self.dur   = 1
        self.parms = [4, 5, 6, 7, 8]
        self.e     = Event(self.start, self.dur, self.parms)

    def test_creation(self):
        self.assertTrue(self.e)

    def test_properties(self):
        self.assertEqual(self.e.at, self.start)
        self.assertEqual(self.e.dur, self.dur)
        self.assertEqual(self.e.parameters, self.parms)

if __name__ == '__main__':
    unittest.main()
