class LogSystem:

    def __init__(self):
        self.entries = []
        self.slices = {
            'Year': 4,
            'Month': 7,
            'Day': 10,
            'Hour': 13,
            'Minute': 16,
            'Second': 19
        }

    def put(self, ident, time):
        self.entries.append((ident, time))

    def retrieve(self, low, high, level):
        length = self.slices[level]
        lo_slice = low[:length]
        hi_slice = high[:length]
        ids = []
        for logid, tstamp in self.entries:
            slice_t = tstamp[:length]
            if lo_slice <= slice_t <= hi_slice:
                ids.append(logid)
        ids.sort()
        return ids
