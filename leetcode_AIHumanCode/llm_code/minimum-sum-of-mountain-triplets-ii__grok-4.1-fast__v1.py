class Solution:
    def minimumSum(self, nums):
        n = len(nums)
        INF = 10**18
        suf_min = [INF] * n
        cur = INF
        for i in range(n - 1, -1, -1):
            suf_min[i] = cur
            cur = min(cur, nums[i])
        res = INF
        pre = INF
        for i in range(n):
            if pre < nums[i] and nums[i] > suf_min[i]:
                res = min(res, pre + nums[i] + suf_min[i])
            pre = min(pre, nums[i])
        return res if res < INF else -1
