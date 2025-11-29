class Solution(object):
    def numGoodSubarrays(self, nums, k):
        freq = {0: 1}
        res = 0
        pre = 0
        idx = 0
        N = len(nums)
        while idx < N:
            v = nums[idx]
            gsum = 0
            end = idx
            while end < N and nums[end] == v:
                gsum = (gsum + v) % k
                now = (pre + gsum) % k
                res += freq.get(now, 0)
                end += 1
            gsum = 0
            ln = end - idx
            for _ in range(ln):
                gsum = (gsum + v) % k
                now = (pre + gsum) % k
                freq[now] = freq.get(now, 0) + 1
            pre = (pre + gsum) % k
            idx = end
        return res
