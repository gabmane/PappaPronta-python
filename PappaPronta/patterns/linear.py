from PappaPronta.patterns.pattern import Pattern

class Linear(Pattern):
    """The Linear class
    
    The Linear class returns a linear interpolation value for any allowed time
    it gets as argument. It has all the methods from its parent class, Pattern.
    """

    def __init__(self, at, dur, startv, endv):
        super(Linear, self).__init__(at, dur)
        self.start_value = startv
        self.end_value = endv
        self.setup()

    def setup(self):
        self.a_factor = (self.end_value - self.start_value) / self.dur
        self.b_factor = self.start_value - (self.a_factor * self.at)


    def next(self, t):
        super(Linear, self).next(t)
        return (self.a_factor*t) + self.b_factor

