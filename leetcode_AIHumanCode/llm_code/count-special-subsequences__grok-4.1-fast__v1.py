from math import gcd

class Solution:
    def numberOfSubsequences(self, nums):
        n = len(nums)
        count = {}
        total = 0
        for curr in range(4, n - 1):
            prev_end = curr - 2
            for idx in range(prev_end - 1):
                x = nums[idx]
                y = nums[prev_end]
                d = gcd(x, y)
                key = (x // d, y // d)
                count[key] = count.get(key, 0) + 1
            for nxt in range(curr + 2, n):
                u = nums[nxt]
                v = nums[curr]
                d = gcd(u, v)
                key = (u // d, v // d)
                total += count.get(key, 0)
        return total
