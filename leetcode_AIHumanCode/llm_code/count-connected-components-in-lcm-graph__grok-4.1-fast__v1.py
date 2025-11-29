class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return
        if self.rank[pi] < self.rank[pj]:
            self.parent[pi] = pj
        elif self.rank[pi] > self.rank[pj]:
            self.parent[pj] = pi
        else:
            self.parent[pj] = pi
            self.rank[pi] += 1


class Solution:
    def countComponents(self, nums, threshold):
        uf = UF(threshold)
        isolated = sum(1 for x in nums if x > threshold)
        components = set()
        for x in nums:
            if x > threshold:
                continue
            pos = x - 1
            multiple = x * 2
            while multiple <= threshold:
                uf.unite(pos, multiple - 1)
                multiple += x
            components.add(uf.find(pos))
        return isolated + len(components)
