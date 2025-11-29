class Solution:
    def maxSubarrayLength(self, nums, k):
        freq = {}
        best = 0
        ptr = 0
        for i in range(len(nums)):
            num = nums[i]
            freq[num] = freq.get(num, 0) + 1
            while freq[num] > k:
                freq[nums[ptr]] -= 1
                ptr += 1
            best = max(best, i - ptr + 1)
        return best
