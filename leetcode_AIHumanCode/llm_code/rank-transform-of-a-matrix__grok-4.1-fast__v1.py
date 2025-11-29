import collections


class UF(object):
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


class Solution(object):
    def matrixRankTransform(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        pos_by_val = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                pos_by_val[matrix[i][j]].append((i, j))
        row_hmax = [0] * m
        col_hmax = [0] * n
        for val in sorted(pos_by_val):
            pts = pos_by_val[val]
            uf = UF(m + n)
            for i, j in pts:
                uf.unite(i, m + j)
            group_max = {}
            for i, j in pts:
                ri = uf.find(i)
                group_max[ri] = max(group_max.get(ri, 0), row_hmax[i])
                ci = uf.find(m + j)
                group_max[ci] = max(group_max.get(ci, 0), col_hmax[j])
            for i, j in pts:
                rt = uf.find(i)
                nxt = group_max[rt] + 1
                matrix[i][j] = nxt
                row_hmax[i] = nxt
                col_hmax[j] = nxt
        return matrix
