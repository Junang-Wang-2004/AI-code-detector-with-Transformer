class Solution(object):
    def minOperations(self, nums, x):
        n = len(nums)
        total = sum(nums)
        req = total - x
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        earliest = {}
        longest = 0
        for j in range(n + 1):
            p = prefix[j]
            look_for = p - req
            if look_for in earliest:
                longest = max(longest, j - earliest[look_for])
            if p not in earliest:
                earliest[p] = j
        return n - longest if longest > 0 else -1
