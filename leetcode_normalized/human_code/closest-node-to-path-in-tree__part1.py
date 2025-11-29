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

        def preprocess(a1, a2):
            D[a1] = 1 if a2 == -1 else D[a2] + 1

        def divide(a1, a2):
            stk.append(partial(postprocess, a1))
            for v1 in reversed(range(len(a1[a1]))):
                v2 = a1[a1][v1]
                if v2 == a2:
                    continue
                stk.append(partial(conquer, v2, a1))
                stk.append(partial(divide, v2, a1))
            stk.append(partial(preprocess, a1, a2))

        def conquer(a1, a2):
            uf.union_set(a1, a2)
            uf.update_ancestor_of_set(a2)

        def postprocess(a1):
            lookup[a1] = True
            for v1 in a2[a1]:
                if not lookup[v1]:
                    continue
                lca[min(a1, v1), max(a1, v1)] = uf.find_ancestor_of_set(v1)
        v1 = len(a1)
        v2, v3, v4 = ([0] * v1, C1(v1), {})
        v5, v6 = ([], [False] * v1)
        v5.append(partial(divide, 0, -1))
        while v5:
            v5.pop()()
        self.D, self.lca = (v2, v4)

class C3(object):

    def closestNode(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            (v1[v3].append(v4), v1[v4].append(v3))
        v5 = collections.defaultdict(set)
        for v6, v7, v8 in a3:
            (v5[v6].add(v7), v5[v7].add(v6))
            (v5[v6].add(v8), v5[v8].add(v6))
            (v5[v7].add(v8), v5[v8].add(v7))
        v9 = C2(v1, v5)
        return [max((v9.lca[min(x, y), max(x, y)] for v10, v11 in ((v6, v7), (v6, v8), (v7, v8))), key=lambda x: v9.D[v10]) for v6, v7, v8 in a3]
