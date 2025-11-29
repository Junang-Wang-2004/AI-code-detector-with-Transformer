import collections

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.set[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.set[v2] = v1
        else:
            self.set[v2] = v1
            self.rank[v1] += 1
        return True

class C2(object):

    def minimumEffortPath(self, a1):
        """
        """

        def index(a1, a2, a3):
            return a2 * a1 + a3
        v1 = []
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if v2 > 0:
                    v1.append((abs(a1[v2][v3] - a1[v2 - 1][v3]), index(len(a1[0]), v2 - 1, v3), index(len(a1[0]), v2, v3)))
                if v3 > 0:
                    v1.append((abs(a1[v2][v3] - a1[v2][v3 - 1]), index(len(a1[0]), v2, v3 - 1), index(len(a1[0]), v2, v3)))
        v1.sort()
        v4 = C1(len(a1) * len(a1[0]))
        for v5, v2, v3 in v1:
            if v4.union_set(v2, v3):
                if v4.find_set(index(len(a1[0]), 0, 0)) == v4.find_set(index(len(a1[0]), len(a1) - 1, len(a1[0]) - 1)):
                    return v5
        return 0
