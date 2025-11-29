# Time:  O(n^2)
# Space: O(n)
# union find
class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
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
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        return True


class Solution5(object):
    def canReachCorner(self, X, Y, circles):
        """
        """
        def check(x1, y1, r1, x2, y2, r2):
            return (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2

        uf = UnionFind(len(circles)+2)
        for u in range(len(circles)):
            x1, y1, r1 = circles[u]
            if x1-r1 <= 0 or y1+r1 >= Y:
                uf.union_set(u, len(circles))
            if x1+r1 >= X or y1-r1 <= 0:
                uf.union_set(u, len(circles)+1)
            for v in range(u):
                x2, y2, r2 = circles[v]
                if not check(x1, y1, r1, x2, y2, r2):
                    continue
                uf.union_set(u, v)
        return uf.find_set(len(circles)) != uf.find_set(len(circles)+1)
