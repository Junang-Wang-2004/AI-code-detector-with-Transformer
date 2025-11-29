# Time:  ctor:  O(mlogm + m * α(n) + nlogn) ~= O(mlogm + nlogn)
#        query: O(α(n) + logn) ~= O(logn)
# Space: O(nlogn + m)

from functools import partial

# Template:
# https://github.com/kamyu104/GoogleKickStart-2020/blob/main/Round%20D/locked_doors.py
class TreeInfos(object):  # Time: O(NlogN), Space: O(NlogN), N is the number of nodes
    def __init__(self, children):
        def preprocess(curr, parent, weight):
            if parent != -1:
                W[curr].append(weight)
                P[curr].append(parent)  # ancestors of the node i
            i = 0
            while i < len(P[curr]) and i < len(P[P[curr][i]]):
                W[curr].append(max(W[curr][i], W[P[curr][i]][i]))
                P[curr].append(P[P[curr][i]][i])
                i += 1
            C[0] += 1
            L[curr] = C[0]  # the subtree of the node i is represented by traversal index L[i]..R[i]

        def divide(curr, parent, weight):
            stk.append(partial(postprocess, curr))
            for child, w in reversed(children[curr]):
                if child == parent:
                    continue
                stk.append(partial(divide, child, curr, w))
            stk.append(partial(preprocess, curr, parent, weight))

        def postprocess(curr):
            R[curr] = C[0]  # the subtree of the node i is represented by traversal index L[i]..R[i]

        N = len(children)
        L, R, P, W, C = [0]*N, [0]*N, [[] for _ in range(N)], [[] for _ in range(N)], [-1]
        for i in range(N):
            if L[i]:
                continue
            stk = []
            stk.append(partial(divide, i, -1, 0))
            while stk:
                stk.pop()()
        self.L, self.R, self.P, self.W = L, R, P, W
    
    def is_ancestor(self, a, b):  # includes itself
        return self.L[a] <= self.L[b] <= self.R[b] <= self.R[a]
    
    def max_weights(self, a, b):
        def binary_lift(a, b):
            w = 0
            for i in reversed(range(len(self.P[a]))):  # O(logN)
                if i < len(self.P[a]) and not self.is_ancestor(self.P[a][i], b):
                    w = max(w, self.W[a][i])
                    a = self.P[a][i]
            return max(w, self.W[a][0])

        w = 0
        if not self.is_ancestor(a, b):
            w = max(w, binary_lift(a, b))
        if not self.is_ancestor(b, a):
            w = max(w, binary_lift(b, a))
        return w

    
class UnionFind(object):  # Time: O(n * α(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0]*n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x_root, y_root = list(map(self.find_set, (x, y)))
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:  # union by rank
            self.set[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.set[y_root] = x_root
        else:
            self.set[y_root] = x_root
            self.rank[x_root] += 1
        return True


class DistanceLimitedPathsExist(object):

    def __init__(self, n, edgeList):
        """
        """
        edgeList.sort(key = lambda x:x[2])
        self.__uf = UnionFind(n)
        self.__adj = [[] for _ in range(n)]
        for index, (i, j, weight) in enumerate(edgeList):
            if not self.__uf.union_set(i, j):
                continue
            self.__adj[i].append((j, weight))
            self.__adj[j].append((i, weight))
        self.__tree_infos = TreeInfos(self.__adj)

    def query(self, p, q, limit):
        """
        """
        if self.__uf.find_set(p) != self.__uf.find_set(q):
            return False
        return self.__tree_infos.max_weights(p, q) < limit


