import collections

class C1(object):

    def __init__(self, a1):
        self.set = list(range(len(a1)))
        self.rank = [0] * len(a1)
        self.cnt = [collections.Counter({v: 1}) for v1 in a1]

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2, a3):
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return 0
        if self.rank[a1] > self.rank[a2]:
            a1, a2 = (a2, a1)
        self.set[a1] = self.set[a2]
        if self.rank[a1] == self.rank[a2]:
            self.rank[a2] += 1
        v3, v4 = (self.cnt[a1][a3], self.cnt[a2][a3])
        self.cnt[a2] = collections.Counter({a3: v3 + v4})
        return v3 * v4

class C2(object):

    def numberOfGoodPaths(self, a1, a2):
        """
        """
        a2.sort(key=lambda x: max(a1[x[0]], a1[x[1]]))
        v1 = C1(a1)
        return len(a1) + sum((v1.union_set(i, j, max(a1[i], a1[j])) for v2, v3 in a2))
