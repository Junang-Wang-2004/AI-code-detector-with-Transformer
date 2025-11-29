import collections
from functools import partial

class C1(object):

    def __init__(self, a1):

        def preprocess(a1, a2, a3):
            D[a1] = 1 if a2 == -1 else D[a2] + 1
            if a2 != -1:
                P[a1].append(a2)
            v1 = 0
            while v1 < len(P[a1]) and v1 < len(P[P[a1][v1]]):
                P[a1].append(P[P[a1][v1]][v1])
                v1 += 1
            C[0] += 1
            L[a1] = C[0]
            if a3 != -1:
                cnt[a3] += 1
            CNT[a1] = cnt[:]

        def divide(a1, a2, a3):
            stk.append(partial(postprocess, a1, a3))
            for v1 in reversed(range(len(a1[a1]))):
                v2, v3 = a1[a1][v1]
                if v2 == a2:
                    continue
                stk.append(partial(divide, v2, a1, v3))
            stk.append(partial(preprocess, a1, a2, a3))

        def postprocess(a1, a2):
            R[a1] = C[0]
            if a2 != -1:
                cnt[a2] -= 1
        v1 = len(a1)
        v2, v3, v4, v5, v6 = ([0] * v1, [0] * v1, [0] * v1, [[] for v7 in range(v1)], [-1])
        v8 = [[0] * MAX_W for v7 in range(v1)]
        v9 = [0] * MAX_W
        v10 = []
        v10.append(partial(divide, 0, -1, -1))
        while v10:
            v10.pop()()
        assert v6[0] == v1 - 1
        self.L, self.R, self.D, self.P = (v2, v3, v4, v5)
        self.CNT = v8

    def is_ancestor(self, a1, a2):
        return self.L[a1] <= self.L[a2] <= self.R[a2] <= self.R[a1]

    def lca(self, a1, a2):
        if self.D[a1] > self.D[a2]:
            a1, a2 = (a2, a1)
        if self.is_ancestor(a1, a2):
            return a1
        for v3 in reversed(range(len(self.P[a1]))):
            if v3 < len(self.P[a1]) and (not self.is_ancestor(self.P[a1][v3], a2)):
                a1 = self.P[a1][v3]
        return self.P[a1][0]
v1 = 26

class C2(object):

    def minOperationsQueries(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v5 -= 1
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = C1(v1)
        v7 = [0] * len(a3)
        for v8, (v9, v10) in enumerate(a3):
            v11 = v6.lca(v9, v10)
            v7[v8] = v6.D[v9] + v6.D[v10] - 2 * v6.D[v11] - max((v6.CNT[v9][v5] + v6.CNT[v10][v5] - 2 * v6.CNT[v11][v5] for v5 in range(v1)))
        return v7
