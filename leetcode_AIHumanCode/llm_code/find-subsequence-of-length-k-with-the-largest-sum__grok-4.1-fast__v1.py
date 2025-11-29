class Solution(object):
    def maxSubsequence(self, nums, k):
        indexed_nums = sorted(enumerate(nums), key=lambda pair: pair[1], reverse=True)[:k]
        sorted_by_pos = sorted(indexed_nums)
        return [value for _, value in sorted_by_pos]
