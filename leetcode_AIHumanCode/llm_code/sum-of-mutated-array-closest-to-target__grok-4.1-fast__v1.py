class Solution:
    def findBestValue(self, arr, target):
        nums = sorted(arr)
        n = len(nums)
        rem = target
        idx = 0
        while idx < n and nums[idx] * (n - idx) <= rem:
            rem -= nums[idx]
            idx += 1
        if idx == n:
            return nums[-1]
        cnt = n - idx
        quot = rem // cnt
        remain = rem % cnt
        return quot if 2 * remain <= cnt else quot + 1
