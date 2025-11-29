class Solution:
    def maximumSumScore(self, nums):
        ans = float('-inf')
        cur_sum = 0
        for num in nums:
            cur_sum += num
            ans = max(ans, cur_sum)
        cur_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            cur_sum += nums[i]
            ans = max(ans, cur_sum)
        return ans
