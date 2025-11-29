import collections

class C1(object):

    def __init__(self, a1, a2):
        self.set = list(range(a1))
        self.rank = [0] * a1
        self.cb = a2

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
            self.cb(v2, v1, v2)
        elif self.rank[v1] > self.rank[v2]:
            self.set[v2] = v1
            self.cb(v1, v1, v2)
        else:
            self.set[v2] = v1
            self.rank[v1] += 1
            self.cb(v1, v1, v2)
        return True

class C2(object):

    def matrixRankTransform(self, a1):
        """
        """

        def cb(a1, a2, a3):
            new_rank[a1] = max(new_rank[a2], new_rank[a3])
        v1 = collections.defaultdict(list)
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                v1[a1[v2][v3]].append([v2, v3])
        v4 = [0] * (len(a1) + len(a1[0]))
        for v5 in sorted(v1):
            v6 = v4[:]
            v7 = C1(len(a1) + len(a1[0]), cb)
            for v2, v3 in v1[v5]:
                v7.union_set(v2, v3 + len(a1))
            for v2, v3 in v1[v5]:
                a1[v2][v3] = v4[v2] = v4[v3 + len(a1)] = v6[v7.find_set(v2)] + 1
        return a1
