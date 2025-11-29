from functools import partial

class C1(object):

    def __init__(self, a1):

        def preprocess(a1, a2):
            D[a1] = 1 if a2 == -1 else D[a2] + 1
            P[a1] = a2

        def divide(a1, a2):
            for v1 in reversed(range(len(a1[a1]))):
                v2 = a1[a1][v1]
                if v2 == a2:
                    continue
                stk.append(partial(divide, v2, a1))
            stk.append(partial(preprocess, a1, a2))
        v1 = len(a1)
        v2, v3 = ([0] * v1, [0] * v1)
        v4 = []
        v4.append(partial(divide, 0, -1))
        while v4:
            v4.pop()()
        self.D, self.P = (v2, v3)

    def lca(self, a1, a2):
        while self.D[a1] > self.D[a2]:
            a1 = self.P[a1]
        while self.D[a1] < self.D[a2]:
            a2 = self.P[a2]
        while a1 != a2:
            a1, a2 = (self.P[a1], self.P[a2])
        return a1

class C2(object):

    def closestNode(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            (v1[v3].append(v4), v1[v4].append(v3))
        v5 = C1(v1)
        return [max((v5.lca(x, y) for v6, v7 in ((start, end), (start, node), (end, node))), key=lambda x: v5.D[v6]) for v8, v9, v10 in a3]
