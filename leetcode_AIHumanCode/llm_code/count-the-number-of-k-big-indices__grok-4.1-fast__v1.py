class Solution:
    def kBigIndices(self, nums, k):
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        def update(tree, idx, val):
            while idx <= m:
                tree[idx] += val
                idx += idx & -idx
        def query(tree, idx):
            res = 0
            while idx > 0:
                res += tree[idx]
                idx -= idx & -idx
            return res
        left_good = [False] * n
        tree = [0] * (m + 2)
        for i in range(n):
            r = rank[nums[i]]
            left_good[i] = query(tree, r - 1) >= k
            update(tree, r, 1)
        right_good = [False] * n
        tree = [0] * (m + 2)
        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]
            right_good[i] = query(tree, r - 1) >= k
            update(tree, r, 1)
        return sum(left_good[i] and right_good[i] for i in range(n))
