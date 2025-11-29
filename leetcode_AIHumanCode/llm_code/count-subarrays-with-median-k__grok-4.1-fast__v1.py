class Solution(object):
    def countSubarrays(self, nums, k):
        pos = nums.index(k)
        def get_score(val):
            if val == k:
                return 0
            elif val < k:
                return -1
            else:
                return 1
        freq = {0: 1}
        pref = 0
        for j in range(pos):
            pref += get_score(nums[j])
            freq[pref] = freq.get(pref, 0) + 1
        pref += get_score(nums[pos])
        res = freq.get(pref, 0) + freq.get(pref - 1, 0)
        for j in range(pos + 1, len(nums)):
            pref += get_score(nums[j])
            res += freq.get(pref, 0) + freq.get(pref - 1, 0)
        return res
