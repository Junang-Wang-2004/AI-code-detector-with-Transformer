import random

class C1:

    def __init__(self, a1):
        self.cumsum = []
        v1 = 0
        for v2 in a1:
            v1 += v2
            self.cumsum.append(v1)
        self.total = v1

    def pickIndex(self):
        v1 = random.randrange(self.total)
        v2, v3 = (0, len(self.cumsum) - 1)
        while v2 < v3:
            v4 = v2 + (v3 - v2) // 2
            if self.cumsum[v4] > v1:
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
