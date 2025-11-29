import collections
from functools import partial

class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1
        self.ancestor = list(range(a1))

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

    def find_ancestor_of_set(self, a1):
        return self.ancestor[self.find_set(a1)]

    def update_ancestor_of_set(self, a1):
        self.ancestor[self.find_set(a1)] = a1

class C2(object):

    def __init__(self, a1, a2):

        def preprocess(a1, a2, a3):
            D[a1] = 1 if a2 == -1 else D[a2] + 1
            if a3 != -1:
                cnt[a3] += 1
            CNT[a1] = cnt[:]

        def divide(a1, a2, a3):
            stk.append(partial(postprocess, a1, a3))
            for v1 in reversed(range(len(a1[a1]))):
                v2, v3 = a1[a1][v1]
                if v2 == a2:
                    continue
                stk.append(partial(conquer, v2, a1))
                stk.append(partial(divide, v2, a1, v3))
            stk.append(partial(preprocess, a1, a2, a3))

        def conquer(a1, a2):
            uf.union_set(a1, a2)
            uf.update_ancestor_of_set(a2)

        def postprocess(a1, a2):
            lookup[a1] = True
            for v1 in a2[a1]:
                if not lookup[v1]:
                    continue
                lca[min(a1, v1), max(a1, v1)] = uf.find_ancestor_of_set(v1)
            if a2 != -1:
                cnt[a2] -= 1
        v1 = len(a1)
        v2, v3, v4 = ([0] * v1, C1(v1), {})
        v5 = [[0] * MAX_W for v6 in range(v1)]
        v7 = [0] * MAX_W
        v8, v9 = ([], [False] * v1)
        v8.append(partial(divide, 0, -1, -1))
        while v8:
            v8.pop()()
        self.D, self.lca = (v2, v4)
        self.CNT = v5
v1 = 26

class C3(object):

    def minOperationsQueries(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v5 -= 1
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = collections.defaultdict(set)
        for v7, v8 in a3:
            (v6[v7].add(v8), v6[v8].add(v7))
        v9 = C2(v1, v6)
        v10 = [0] * len(a3)
        for v11, (v7, v8) in enumerate(a3):
            v12 = v9.lca[min(v7, v8), max(v7, v8)]
            v10[v11] = v9.D[v7] + v9.D[v8] - 2 * v9.D[v12] - max((v9.CNT[v7][v5] + v9.CNT[v8][v5] - 2 * v9.CNT[v12][v5] for v5 in range(v1)))
        return v10
