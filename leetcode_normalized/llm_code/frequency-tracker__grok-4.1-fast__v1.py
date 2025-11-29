class C1:

    def __init__(self):
        self.counts = {}
        self.met = {}

    def add(self, a1):
        v1 = self.counts.get(a1, 0)
        if v1 > 0:
            self.met[v1] -= 1
            if self.met[v1] == 0:
                del self.met[v1]
        self.counts[a1] = v1 + 1
        v2 = self.counts[a1]
        self.met[v2] = self.met.get(v2, 0) + 1

    def deleteOne(self, a1):
        v1 = self.counts.get(a1, 0)
        if v1 == 0:
            return
        self.met[v1] -= 1
        if self.met[v1] == 0:
            del self.met[v1]
        self.counts[a1] = v1 - 1
        v2 = self.counts[a1]
        if v2 > 0:
            self.met[v2] = self.met.get(v2, 0) + 1
        else:
            del self.counts[a1]

    def hasFrequency(self, a1):
        return a1 in self.met
