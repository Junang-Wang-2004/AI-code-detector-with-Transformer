class C1:

    def __init__(self, a1, a2):
        self.source = a1
        self.size = len(a1)
        self.want = a2
        self.picks = list(range(a2))
        self.finished = False

    def next(self):
        v1 = ''.join((self.source[idx] for v2 in self.picks))
        v3 = self.want - 1
        while v3 >= 0 and self.picks[v3] == self.size - self.want + v3:
            v3 -= 1
        if v3 < 0:
            self.finished = True
        else:
            self.picks[v3] += 1
            for v4 in range(v3 + 1, self.want):
                self.picks[v4] = self.picks[v4 - 1] + 1
        return v1

    def hasNext(self):
        return not self.finished
