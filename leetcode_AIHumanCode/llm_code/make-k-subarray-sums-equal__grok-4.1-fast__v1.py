from math import gcd

class Solution:
    def makeSubKSumEqual(self, nums, goal):
        size = len(nums)
        div = gcd(goal, size)
        ans = 0
        for start in range(div):
            chunk = nums[start::div]
            sorted_chunk = sorted(chunk)
            mid_idx = len(sorted_chunk) // 2
            median = sorted_chunk[mid_idx]
            ans += sum(abs(val - median) for val in chunk)
        return ans
