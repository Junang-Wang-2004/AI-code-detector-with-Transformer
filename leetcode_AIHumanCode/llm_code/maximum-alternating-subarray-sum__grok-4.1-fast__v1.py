class Solution:
    def maximumAlternatingSubarraySum(self, nums):
        ans = float('-inf')
        prev_pos = float('-inf')
        prev_neg = float('-inf')
        for num in nums:
            curr_pos = num
            if prev_neg != float('-inf'):
                curr_pos = max(curr_pos, prev_neg + num)
            curr_neg = float('-inf')
            if prev_pos != float('-inf'):
                curr_neg = prev_pos - num
            ans = max(ans, curr_pos, curr_neg)
            prev_pos = curr_pos
            prev_neg = curr_neg
        return ans
