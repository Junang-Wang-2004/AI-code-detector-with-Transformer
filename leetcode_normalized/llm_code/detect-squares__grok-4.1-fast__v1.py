from collections import defaultdict

class C1:

    def __init__(self):
        self.point_count = defaultdict(lambda: defaultdict(int))

    def add(self, a1):
        v1, v2 = a1
        self.point_count[v1][v2] += 1

    def count(self, a1):
        v1, v2 = a1
        v3 = 0
        v4 = list(self.point_count[v1])
        for v5 in v4:
            if v5 == v2:
                continue
            v6 = abs(v5 - v2)
            v3 += self.point_count[v1][v5] * self.point_count[v1 + v6][v2] * self.point_count[v1 + v6][v5]
            v3 += self.point_count[v1][v5] * self.point_count[v1 - v6][v2] * self.point_count[v1 - v6][v5]
        return v3
