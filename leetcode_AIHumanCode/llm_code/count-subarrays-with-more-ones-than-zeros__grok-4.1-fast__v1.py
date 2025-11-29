class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0:
            return 0
        offset = n + 1
        ft = FenwickTree(2 * n + 2)
        ft.update(offset, 1)
        pref = 0
        ans = 0
        for val in nums:
            pref += 1 if val == 0 else -1
            ans = (ans + ft.query(offset + pref - 1)) % MOD
            ft.update(offset + pref, 1)
        return ans
