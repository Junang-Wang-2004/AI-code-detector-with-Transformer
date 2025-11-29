class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        if not nums:
            return 0
        mx = max(nums)
        length = 0
        temp = 1
        while temp <= mx:
            length += 1
            temp <<= 1
        counts = [0] * length
        for val in nums:
            pos = 0
            nval = val
            while nval > 0:
                if nval & 1:
                    counts[pos] += 1
                pos += 1
                nval >>= 1
        result = 0
        for threshold in range(1, k + 1):
            value = 0
            for pos in range(length):
                if counts[pos] >= threshold:
                    value += 1 << pos
            result = (result + value * value) % MOD
        return result
