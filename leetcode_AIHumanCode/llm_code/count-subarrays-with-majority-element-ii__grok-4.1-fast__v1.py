class Solution:
    def countMajoritySubarrays(self, nums, target):
        class FenwickTree:
            def __init__(self, sz):
                self.sz = sz
                self.tree = [0] * (sz + 1)

            def update(self, i, val):
                i += 1
                while i <= self.sz:
                    self.tree[i] += val
                    i += i & -i

            def query(self, i):
                i += 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res

        n = len(nums)
        if n == 0:
            return 0
        ft = FenwickTree(2 * n + 1)
        offset = n
        balance = 0
        ft.update(offset, 1)
        ans = 0
        for x in nums:
            balance += 1 if x == target else -1
            ans += ft.query(balance - 1 + offset)
            ft.update(balance + offset, 1)
        return ans
