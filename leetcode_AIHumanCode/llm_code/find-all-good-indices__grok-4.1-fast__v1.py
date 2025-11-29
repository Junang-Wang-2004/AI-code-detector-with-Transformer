class Solution(object):
    def goodIndices(self, nums, k):
        n = len(nums)
        ldp = [1] * n
        for j in range(1, n):
            if nums[j] <= nums[j - 1]:
                ldp[j] = ldp[j - 1] + 1
        rdp = [1] * n
        for j in range(n - 2, -1, -1):
            if nums[j] <= nums[j + 1]:
                rdp[j] = rdp[j + 1] + 1
        res = []
        for idx in range(k, n - k):
            if ldp[idx - 1] >= k and rdp[idx + 1] >= k:
                res.append(idx)
        return res
