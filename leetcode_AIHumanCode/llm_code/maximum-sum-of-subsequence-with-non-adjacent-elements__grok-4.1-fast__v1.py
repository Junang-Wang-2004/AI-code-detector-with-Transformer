class Solution:
    def maximumSumSubsequence(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        tree = [[0] * 4 for _ in range(4 * n)]

        def merge(a, b):
            res = [0] * 4
            res[0] = max(a[2] + b[1], a[0] + b[1], a[2] + b[0])
            res[1] = max(a[3] + b[1], a[1] + b[1], a[3] + b[0])
            res[2] = max(a[2] + b[3], a[0] + b[3], a[2] + b[2])
            res[3] = max(a[3] + b[3], a[1] + b[3], a[3] + b[2])
            return res

        def construct(node, lo, hi):
            if lo == hi:
                val = max(nums[lo], 0)
                tree[node] = [val, 0, 0, 0]
                return
            mid = (lo + hi) // 2
            construct(2 * node, lo, mid)
            construct(2 * node + 1, mid + 1, hi)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def modify(node, lo, hi, idx, val):
            if lo == hi:
                val = max(val, 0)
                tree[node] = [val, 0, 0, 0]
                return
            mid = (lo + hi) // 2
            if idx <= mid:
                modify(2 * node, lo, mid, idx, val)
            else:
                modify(2 * node + 1, mid + 1, hi, idx, val)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        construct(1, 0, n - 1)
        result = 0
        for idx, val in queries:
            modify(1, 0, n - 1, idx, val)
            result = (result + max(tree[1])) % MOD
        return result
