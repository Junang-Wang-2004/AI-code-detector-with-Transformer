class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        if not nums:
            return False
        maximum = 0
        prior_length = 0
        idx = 0
        n = len(nums)
        while idx < n:
            begin = idx
            while idx + 1 < n and nums[idx] < nums[idx + 1]:
                idx += 1
            segment_size = idx - begin + 1
            maximum = max(maximum, segment_size // 2)
            if prior_length > 0:
                maximum = max(maximum, min(prior_length, segment_size))
            prior_length = segment_size
            idx += 1
        return maximum >= k
