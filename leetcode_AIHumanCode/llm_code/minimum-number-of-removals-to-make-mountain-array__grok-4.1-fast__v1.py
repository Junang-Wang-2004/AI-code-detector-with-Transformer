import bisect

class Solution:
    def minimumMountainRemovals(self, nums):
        n = len(nums)
        inc_end = [0] * n
        tails = []
        for i in range(n):
            idx = bisect.bisect_left(tails, nums[i])
            inc_end[i] = idx + 1
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
        dec_start = [0] * n
        tails = []
        for i in range(n - 1, -1, -1):
            idx = bisect.bisect_left(tails, nums[i])
            dec_start[i] = idx + 1
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
        max_mtn = 1
        for i in range(1, n - 1):
            max_mtn = max(max_mtn, inc_end[i] + dec_start[i] - 1)
        return n - max_mtn
