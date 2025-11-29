class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        class SegTree(object):
            def __init__(self, size):
                self.mod = 10**9 + 7
                self.size = size
                self.tree = [0] * (4 * size)
                self.lazy = [0] * (4 * size)

            def propagate(self, node, start, end):
                if self.lazy[node] != 0:
                    self.tree[node] = (self.tree[node] + self.lazy[node] * (end - start + 1)) % self.mod
                    if start !=
