import collections
import itertools

class C1(object):

    def __init__(self):
        self.set = {}
        self.rank = collections.Counter()

    def find_set(self, a1):
        v1, v2 = self.set.setdefault(a1, (a1, 1.0))
        if a1 != v1:
            v3, v4 = self.find_set(v1)
            self.set[a1] = (v3, v2 * v4)
        return self.set[a1]

    def union_set(self, a1, a2, a3):
        (v1, v2), (v3, v4) = list(map(self.find_set, (a1, a2)))
        if v1 == v3:
            return False
        if self.rank[v1] < self.rank[v3]:
            self.set[v1] = (v3, a3 * v4 / v2)
        elif self.rank[v1] > self.rank[v3]:
            self.set[v3] = (v1, 1.0 / a3 * v2 / v4)
        else:
            self.set[v3] = (v1, 1.0 / a3 * v2 / v4)
            self.rank[v1] += 1
        return True

    def query_set(self, a1, a2):
        if a1 not in self.set or a2 not in self.set:
            return -1.0
        (v1, v2), (v3, v4) = list(map(self.find_set, (a1, a2)))
        return v2 / v4 if v1 == v3 else -1.0
