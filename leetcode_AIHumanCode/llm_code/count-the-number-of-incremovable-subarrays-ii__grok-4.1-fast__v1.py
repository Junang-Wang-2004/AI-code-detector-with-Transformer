class Solution(object):
    def incremovableSubarrayCount(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        pref = 0
        while pref < n - 1 and nums[pref] < nums[pref + 1]:
            pref += 1
        suf = n - 1
        while suf > 0 and nums[suf - 1] < nums[suf]:
            suf -= 1
        if pref == n - 1 and suf == 0:
            return n * (n + 1) // 2
        total = n - suf + 1
        pos = suf
        for idx in range(pref + 1):
            while pos < n and not (nums[idx] < nums[pos]):
                pos += 1
            total += n - pos + 1
        return total
