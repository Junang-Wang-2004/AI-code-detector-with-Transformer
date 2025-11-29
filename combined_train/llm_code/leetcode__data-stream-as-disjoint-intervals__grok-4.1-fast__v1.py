class C1(object):

    def __init__(self, a1=0, a2=0):
        self.start = a1
        self.end = a2

class C2(object):

    def __init__(self):
        self._ranges = []

    def addNum(self, a1):
        v1, v2 = (0, len(self._ranges))
        while v1 < v2:
            v3 = v1 + (v2 - v1) // 2
            if self._ranges[v3][0] > a1:
                v2 = v3
            else:
                v1 = v3 + 1
        v4 = v1
        v5 = v4 > 0 and self._ranges[v4 - 1][1] + 1 >= a1
        if v5:
            v4 -= 1
            v6 = self._ranges[v4][0]
            v7 = max(self._ranges[v4][1], a1)
        else:
            v6 = a1
            v7 = a1
        while v4 < len(self._ranges) and self._ranges[v4][0] <= v7 + 1:
            v6 = min(v6, self._ranges[v4][0])
            v7 = max(v7, self._ranges[v4][1])
            del self._ranges[v4]
        self._ranges.insert(v4, [v6, v7])

    def getIntervals(self):
        return [C1(rng[0], rng[1]) for v1 in self._ranges]
