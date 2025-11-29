class Solution(object):
    def binarySearchableNumbers(self, nums):
        n = len(nums)
        pre = [float('-inf')] * n
        if n > 0:
            pre[0] = nums[0]
            for i in range(1, n):
                pre[i] = max(pre[i - 1], nums[i])
        suf = [float('inf')] * n
        if n > 0:
            suf[n - 1] = nums[n - 1]
            for i in range(n - 2, -1, -1):
                suf[i] = min(suf[i + 1], nums[i])
        unique = set()
        for i in range(n):
            lbound = float('-inf') if i == 0 else pre[i - 1]
            rbound = float('inf') if i == n - 1 else suf[i + 1]
            if lbound <= nums[i] <= rbound:
                unique.add(nums[i])
        return len(unique)
