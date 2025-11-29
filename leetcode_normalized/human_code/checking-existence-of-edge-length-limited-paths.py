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

    def distanceLimitedPathsExist(self, a1, a2, a3):
        """
        """
        for v1, v2 in enumerate(a3):
            v2.append(v1)
        a2.sort(key=lambda x: x[2])
        a3.sort(key=lambda x: x[2])
        v3 = C1(a1)
        v4 = [False] * len(a3)
        v5 = 0
        for v6, v7, v8, v1 in a3:
            while v5 < len(a2) and a2[v5][2] < v8:
                v3.union_set(a2[v5][0], a2[v5][1])
                v5 += 1
            v4[v1] = v3.find_set(v6) == v3.find_set(v7)
        return v4
