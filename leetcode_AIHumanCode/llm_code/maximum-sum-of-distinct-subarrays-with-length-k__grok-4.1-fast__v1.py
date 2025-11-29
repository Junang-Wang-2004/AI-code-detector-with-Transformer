from collections import Counter

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        if n < k:
            return 0
        freq = Counter()
        window_sum = 0
        ans = 0
        for i in range(k):
            freq[nums[i]] += 1
            window_sum += nums[i]
        if len(freq) == k:
            ans = window_sum
        for i in range(k, n):
            prev = nums[i - k]
            freq[prev] -= 1
            if freq[prev] == 0:
                del freq[prev]
            window_sum -= prev
            nxt = nums[i]
            freq[nxt] += 1
            window_sum += nxt
            if len(freq) == k:
                ans = max(ans, window_sum)
        return ans
