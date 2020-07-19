class Pattern:
    """The Pattern class
    
    The Pattern class is the base class for all sequencing objects.
    It has only basic properties:
        * action time: start of validity
        * duration: the duration of validity
    It has only basic methods:
        * next(t): gets the next event at time t
        * end(): gets the end time for events
        * check_time(t): checks whether t falls between at and endt
    """

    def __init__(self, at, dur):
        self.at = at
        self.dur = dur

    def end(self):
        return self.at + self.dur

    def next(self, t):
        try:
            self.check_time(t)
        except:
            print('time t (%f) must be between %f and %f' % (t, self.at, self.end()))
        finally:
            return None

    def check_time(self, t):
        return True if (t >= self.at and t <= self.end()) else False
