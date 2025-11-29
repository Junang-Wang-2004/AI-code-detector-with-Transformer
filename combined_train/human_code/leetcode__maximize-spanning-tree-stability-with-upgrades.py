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
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return False
        if self.rank[a1] > self.rank[a2]:
            a1, a2 = (a2, a1)
        self.set[a1] = self.set[a2]
        if self.rank[a1] == self.rank[a2]:
            self.rank[a2] += 1
        return True

class C2(object):

    def maxStability(self, a1, a2, a3):
        """
        """
        v1 = C1(a1)
        v2 = 0
        v3 = float('inf')
        for v4, v5, v6, v7 in a2:
            if not v7:
                continue
            if not v1.union_set(v4, v5):
                return -1
            v2 += 1
            v3 = min(v3, v6)
        a2.sort(key=lambda x: -x[2])
        for v4, v5, v6, v7 in a2:
            if v7:
                continue
            if not v1.union_set(v4, v5):
                continue
            v2 += 1
            if v2 == a1 - 1 - a3:
                v3 = min(v3, v6)
            elif v2 == a1 - 1:
                v3 = min(v3, 2 * v6)
        return v3 if v2 == a1 - 1 else -1
