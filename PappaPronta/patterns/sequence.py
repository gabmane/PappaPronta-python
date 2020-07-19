from PappaPronta.patterns.pattern import Pattern

class Sequence(Pattern):
    """The Sequence class
    
    The Sequence class returns a sequence of values at each next() call,
    regardless of the time (which has to be legal though).
    It has all the methods from its parent class, Pattern.
    """

    def __init__(self, at, dur, values):
        super(Sequence, self).__init__(at, dur)
        self.values = values
        self.setup()

    def setup(self):
        self.index = 0
        self.size = len(self.values)


    def next(self, t):
        super(Sequence, self).next(t)
        result = self.values[self.index]
        self.index += 1
        if (self.index >= self.size):
            self.index = 0
        return result
