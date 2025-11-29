import bisect

class Solution(object):
    def minOperations(self, nums):
        ops = 0
        tails = [0]
        for val in nums:
            idx = bisect.bisect_right(tails, val)
            tails = tails[:idx]
            if tails[-1] < val:
                ops += 1
                tails.append(val)
        return ops
