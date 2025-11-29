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

    def minimumHammingDistance(self, a1, a2, a3):
        """
        """
        v1 = C1(len(a1))
        for v2, v3 in a3:
            v1.union_set(v2, v3)
        v4 = collections.defaultdict(set)
        for v5 in range(len(a1)):
            v4[v1.find_set(v5)].add(v5)
        v6 = 0
        for v7 in v4.values():
            v8 = collections.Counter([a1[v5] for v5 in v7])
            v9 = collections.Counter([a2[v5] for v5 in v7])
            v10 = v8 - v9
            v6 += sum(v10.values())
        return v6
