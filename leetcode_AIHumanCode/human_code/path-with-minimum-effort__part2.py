# Time:  O(m * n * log(m * n) + m * n * α(m * n)) = O(m * n * log(m * n))
# Space: O(m * n)
import collections


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


# union find solution
class Solution2(object):
    def minimumEffortPath(self, heights):
        """
        """
        def index(n, i, j):
            return i*n + j
    
        diffs = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i > 0:
                    diffs.append((abs(heights[i][j]-heights[i-1][j]), index(len(heights[0]), i-1, j), index(len(heights[0]), i, j)))
                if j > 0:
                    diffs.append((abs(heights[i][j]-heights[i][j-1]), index(len(heights[0]), i, j-1), index(len(heights[0]), i, j)))
        diffs.sort()
        union_find = UnionFind(len(heights)*len(heights[0]))
        for d, i, j in diffs:
            if union_find.union_set(i, j):
                if union_find.find_set(index(len(heights[0]), 0, 0)) == \
                   union_find.find_set(index(len(heights[0]), len(heights)-1, len(heights[0])-1)):
                    return d
        return 0


