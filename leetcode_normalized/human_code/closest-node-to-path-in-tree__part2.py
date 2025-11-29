from functools import partial

class C1(object):

    def __init__(self, a1):

        def preprocess(a1, a2):
            D[a1] = 1 if a2 == -1 else D[a2] + 1
            if a2 != -1:
                P[a1].append(a2)
            v1 = 0
            while v1 < len(P[a1]) and v1 < len(P[P[a1][v1]]):
                P[a1].append(P[P[a1][v1]][v1])
                v1 += 1
            C[0] += 1
            L[a1] = C[0]

        def divide(a1, a2):
            stk.append(partial(postprocess, a1))
            for v1 in reversed(range(len(a1[a1]))):
                v2 = a1[a1][v1]
                if v2 == a2:
                    continue
                stk.append(partial(divide, v2, a1))
            stk.append(partial(preprocess, a1, a2))

        def postprocess(a1):
            R[a1] = C[0]
        v1 = len(a1)
        v2, v3, v4, v5, v6 = ([0] * v1, [0] * v1, [0] * v1, [[] for v7 in range(v1)], [-1])
        v8 = []
        v8.append(partial(divide, 0, -1))
        while v8:
            v8.pop()()
        assert v6[0] == v1 - 1
        self.L, self.R, self.D, self.P = (v2, v3, v4, v5)

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

class C2(object):

    def closestNode(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            (v1[v3].append(v4), v1[v4].append(v3))
        v5 = C1(v1)
        return [max((v5.lca(x, y) for v6, v7 in ((start, end), (start, node), (end, node))), key=lambda x: v5.D[v6]) for v8, v9, v10 in a3]
