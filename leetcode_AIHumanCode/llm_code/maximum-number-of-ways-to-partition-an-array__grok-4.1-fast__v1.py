import collections

class Solution:
    def waysToPartition(self, nums, k):
        n = len(nums)
        s = sum(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]
        fr = collections.Counter(2 * ps[i] - s for i in range(1, n))
        mx = fr[0]
        lf = collections.Counter()
        for j in range(n):
            x = nums[j]
            mx = max(mx, lf[k - x] + fr[x - k])
            if j < n - 1:
                d = 2 * ps[j + 1] - s
                lf[d] += 1
                fr[d] -= 1
        return mx
