import bisect

class C1:

    def __init__(self):
        self.data = []
        self.total = 0

    def add(self, a1, a2):
        v1 = bisect.bisect_left(self.data, (a1,))
        if v1 > 0 and self.data[v1 - 1][1] >= a1 - 1:
            v1 -= 1
            a1 = self.data[v1][0]
        v3 = a2
        v4 = v1
        while v4 < len(self.data) and self.data[v4][0] <= v3 + 1:
            v3 = max(v3, self.data[v4][1])
            self.total -= self.data[v4][1] - self.data[v4][0] + 1
            v4 += 1
        del self.data[v1:v4]
        self.data.insert(v1, (a1, v3))
        self.total += v3 - a1 + 1

    def count(self):
        return self.total
