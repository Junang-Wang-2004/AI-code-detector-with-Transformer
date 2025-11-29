class DSU:
    def __init__(self, arr):
        n = len(arr)
        self.parent = list(range(n))
        self.rank = [0] * n
        self.comp_sum = arr[:]

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        cur = x
        while cur != root:
            nxt = self.parent[cur]
            self.parent[cur] = root
            cur = nxt
        return root

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
            self.comp_sum[pb] += self.comp_sum[pa]
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.comp_sum[pa] += self.comp_sum[pb]
        else:
            self.parent[pb] = pa
            self.comp_sum[pa] += self.comp_sum[pb]
            self.rank[pa] += 1
        return True

    def get_sum(self, x):
        return self.comp_sum[self.find(x)]


class Solution:
    def maximumSegmentSum(self, nums, removeQueries):
        n = len(nums)
        ans = [0] * n
        active = [False] * n
        dsu = DSU(nums)
        for step in range(1, n):
            pos = removeQueries[n - step]
            active[pos] = True
            if pos > 0 and active[pos - 1]:
                dsu.unite(pos - 1, pos)
            if pos + 1 < n and active[pos + 1]:
                dsu.unite(pos, pos + 1)
            ans[n - step - 1] = max(ans[n - step], dsu.get_sum(pos))
        return ans
