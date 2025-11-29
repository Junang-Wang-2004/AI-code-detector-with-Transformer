class Solution:
    def createTargetArray(self, nums, index):
        target = []
        n = len(nums)
        for i in range(n):
            pos = index[i]
            target = target[:pos] + [nums[i]] + target[pos:]
        return target
