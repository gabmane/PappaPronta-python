from PappaPronta.patterns.pattern import Pattern

class Constant(Pattern):
    """The Constant class
    
    The Constant class returns the same value for any allowed time it gets
    in the input. It has all the methods from its parent class, Pattern.
    """

    def __init__(self, at, dur, value):
        super(Constant, self).__init__(at, dur)
        self.value = value

    def next(self, t):
        super(Constant, self).next(t)
        return self.value
