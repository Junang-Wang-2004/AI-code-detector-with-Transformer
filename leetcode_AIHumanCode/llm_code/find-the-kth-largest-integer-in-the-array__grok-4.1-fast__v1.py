class Solution(object):
    def kthLargestNumber(self, nums, k):
        sorted_nums = sorted(nums, key=lambda s: (len(s), s), reverse=True)
        return sorted_nums[k - 1]
