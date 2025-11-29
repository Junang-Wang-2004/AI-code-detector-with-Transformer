# Time:  O(nlogn)
# Space: O(1)
# codeforce, https://codeforces.com/contest/1782/problem/B
# sort, greedy
class Solution2(object):
    def countWays(self, nums):
        """
        """
        nums.sort()
        return sum((i == 0 or nums[i-1] < i) and (i == len(nums) or nums[i] > i) for i in range(len(nums)+1))
