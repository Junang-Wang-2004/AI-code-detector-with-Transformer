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

    def minCostConnectPoints(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1)):
            for v3 in range(v2 + 1, len(a1)):
                v1.append((v2, v3, abs(a1[v3][0] - a1[v2][0]) + abs(a1[v3][1] - a1[v2][1])))
        v1.sort(key=lambda x: x[2])
        v4 = 0
        v5 = C1(len(a1))
        for v2, v3, v6 in v1:
            if v5.union_set(v2, v3):
                v4 += v6
        return v4
