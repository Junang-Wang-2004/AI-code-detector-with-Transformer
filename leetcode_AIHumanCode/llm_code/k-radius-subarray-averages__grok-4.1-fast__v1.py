class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        ans = [-1] * n
        window = 2 * k + 1
        if n < window:
            return ans
        cur = sum(nums[:window])
        ans[k] = cur // window
        for center in range(k + 1, n - k):
            cur -= nums[center - k - 1]
            cur += nums[center + k]
            ans[center] = cur // window
        return ans
