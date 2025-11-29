class Solution:
    def numberOfSubarrays(self, nums, k):
        freq = {0: 1}
        pref = 0
        ans = 0
        for val in nums:
            pref += val % 2
            ans += freq.get(pref - k, 0)
            freq[pref] = freq.get(pref, 0) + 1
        return ans
