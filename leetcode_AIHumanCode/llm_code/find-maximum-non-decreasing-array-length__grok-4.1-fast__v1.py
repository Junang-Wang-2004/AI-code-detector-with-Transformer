class Solution(object):
    def findMaximumLength(self, nums):
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        longest = [0] * (n + 1)
        ptr = 0
        for i in range(1, n + 1):
            while ptr + 1 < i and pref[i] > 2 * pref[ptr + 1]:
                ptr += 1
            longest[i] = longest[ptr] + 1
        return longest[n]
