class Solution:
    def numOfSubarrays(self, nums, k, threshold):
        ans = 0
        win = sum(nums[:k])
        if win >= k * threshold:
            ans += 1
        for start in range(k, len(nums)):
            win += nums[start] - nums[start - k]
            if win >= k * threshold:
                ans += 1
        return ans
