class Event(object):
    """The Event class
    
    The Event class is the base class for all Event (output) objects.
    It has only basic properties:
        * action time: start of validity
        * duration: the duration of validity
        * parameters: an array of other, user-defined, parameters
    It has only basic methods:
        * end(): gets the end time for events
    """

    def __init__(self, at, dur, parms):
        self.at = at
        self.dur = dur
        self.parameters = parms

    def end(self):
        return self.at + self.dur

    def output(self):
        return "Event: action time %8.4f, dur %8.4f" % (self.at, self.dur)
