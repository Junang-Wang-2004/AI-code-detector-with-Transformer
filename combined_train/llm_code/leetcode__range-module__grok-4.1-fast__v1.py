import bisect

class C1:

    def __init__(self):
        self.ranges = []

    def addRange(self, a1, a2):
        v1 = 0
        v2 = len(self.ranges)
        v3 = []
        while v1 < v2 and self.ranges[v1][1] < a1:
            v3.append(self.ranges[v1])
            v1 += 1
        v4 = a1
        v5 = a2
        while v1 < v2 and self.ranges[v1][0] <= v5:
            v4 = min(v4, self.ranges[v1][0])
            v5 = max(v5, self.ranges[v1][1])
            v1 += 1
        v3.append((v4, v5))
        self.ranges = v3 + self.ranges[v1:]

    def queryRange(self, a1, a2):
        v1 = bisect.bisect_right(self.ranges, (a1, float('inf'))) - 1
        return v1 >= 0 and self.ranges[v1][1] >= a2

    def removeRange(self, a1, a2):
        v1 = []
        for v2 in self.ranges:
            v3, v4 = v2
            if v4 <= a1 or v3 >= a2:
                v1.append(v2)
            else:
                if v3 < a1:
                    v1.append((v3, a1))
                if a2 < v4:
                    v1.append((a2, v4))
        self.ranges = v1
