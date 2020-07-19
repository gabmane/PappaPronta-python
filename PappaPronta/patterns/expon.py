from math import exp, log
from PappaPronta.patterns.pattern import Pattern

class Expon(Pattern):
    """The Expon class
    
    The Expon class returns an exponential interpolation value for any allowed time
    it gets as argument. It has all the methods from its parent class, Pattern.
    """

    def __init__(self, at, dur, startv, endv):
        super(Expon, self).__init__(at, dur)
        self.start_value = startv
        self.end_value = endv
        self.setup()

    def setup(self):
        self.a_factor = (log(self.end_value) - log(self.start_value)) / self.dur
        self.b_factor = log(self.start_value) - (self.a_factor * self.at)

    def next(self, t):
        super(Expon, self).next(t)
        return exp((self.a_factor*t) + self.b_factor)
