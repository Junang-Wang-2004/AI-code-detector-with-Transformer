from functools import partial

class C1(object):

    def __init__(self, a1):

        def preprocess(a1, a2, a3):
            if a2 != -1:
                W[a1].append(a3)
                P[a1].append(a2)
            v1 = 0
            while v1 < len(P[a1]) and v1 < len(P[P[a1][v1]]):
                W[a1].append(max(W[a1][v1], W[P[a1][v1]][v1]))
                P[a1].append(P[P[a1][v1]][v1])
                v1 += 1
            C[0] += 1
            L[a1] = C[0]

        def divide(a1, a2, a3):
            stk.append(partial(postprocess, a1))
            for v1, v2 in reversed(a1[a1]):
                if v1 == a2:
                    continue
                stk.append(partial(divide, v1, a1, v2))
            stk.append(partial(preprocess, a1, a2, a3))

        def postprocess(a1):
            R[a1] = C[0]
        v1 = len(a1)
        v2, v3, v4, v5, v6 = ([0] * v1, [0] * v1, [[] for v7 in range(v1)], [[] for v7 in range(v1)], [-1])
        for v8 in range(v1):
            if v2[v8]:
                continue
            v9 = []
            v9.append(partial(divide, v8, -1, 0))
            while v9:
                v9.pop()()
        self.L, self.R, self.P, self.W = (v2, v3, v4, v5)

    def is_ancestor(self, a1, a2):
        return self.L[a1] <= self.L[a2] <= self.R[a2] <= self.R[a1]

    def max_weights(self, a1, a2):

        def binary_lift(a1, a2):
            v1 = 0
            for v2 in reversed(range(len(self.P[a1]))):
                if v2 < len(self.P[a1]) and (not self.is_ancestor(self.P[a1][v2], a2)):
                    v1 = max(v1, self.W[a1][v2])
                    a1 = self.P[a1][v2]
            return max(v1, self.W[a1][0])
        v1 = 0
        if not self.is_ancestor(a1, a2):
            v1 = max(v1, binary_lift(a1, a2))
        if not self.is_ancestor(a2, a1):
            v1 = max(v1, binary_lift(a2, a1))
        return v1

class C2(object):

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

class C3(object):

    def __init__(self, a1, a2):
        """
        """
        a2.sort(key=lambda x: x[2])
        self.__uf = C2(a1)
        self.__adj = [[] for v1 in range(a1)]
        for v2, (v3, v4, v5) in enumerate(a2):
            if not self.__uf.union_set(v3, v4):
                continue
            self.__adj[v3].append((v4, v5))
            self.__adj[v4].append((v3, v5))
        self.__tree_infos = C1(self.__adj)

    def query(self, a1, a2, a3):
        """
        """
        if self.__uf.find_set(a1) != self.__uf.find_set(a2):
            return False
        return self.__tree_infos.max_weights(a1, a2) < a3
