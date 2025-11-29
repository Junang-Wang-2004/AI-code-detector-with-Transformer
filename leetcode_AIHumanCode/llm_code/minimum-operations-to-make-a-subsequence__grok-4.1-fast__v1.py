class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] = max(self.tree[index], value)
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result = max(result, self.tree[index])
            index -= index & -index
        return result


class Solution:
    def minOperations(self, target, arr):
        n = len(target)
        if n == 0:
            return 0
        index_map = {target[i]: i + 1 for i in range(n)}
        ft = FenwickTree(n)
        for val in arr:
            if val in index_map:
                pos = index_map[val]
                prior_max = ft.query(pos - 1)
                ft.update(pos, prior_max + 1)
        longest = ft.query(n)
        return n - longest
