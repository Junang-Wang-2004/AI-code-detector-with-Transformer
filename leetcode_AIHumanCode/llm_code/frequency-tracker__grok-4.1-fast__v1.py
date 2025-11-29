class FrequencyTracker:

    def __init__(self):
        self.counts = {}
        self.met = {}

    def add(self, num):
        prev = self.counts.get(num, 0)
        if prev > 0:
            self.met[prev] -= 1
            if self.met[prev] == 0:
                del self.met[prev]
        self.counts[num] = prev + 1
        curr = self.counts[num]
        self.met[curr] = self.met.get(curr, 0) + 1

    def deleteOne(self, num):
        prev = self.counts.get(num, 0)
        if prev == 0:
            return
        self.met[prev] -= 1
        if self.met[prev] == 0:
            del self.met[prev]
        self.counts[num] = prev - 1
        curr = self.counts[num]
        if curr > 0:
            self.met[curr] = self.met.get(curr, 0) + 1
        else:
            del self.counts[num]

    def hasFrequency(self, f):
        return f in self.met
