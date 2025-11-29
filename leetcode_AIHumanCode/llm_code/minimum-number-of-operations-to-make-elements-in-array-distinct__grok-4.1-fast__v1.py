class Solution:
    def minimumOperations(self, nums):
        n = len(nums)
        appeared = set()
        for idx in range(n - 1, -1, -1):
            if nums[idx] in appeared:
                return (idx + 1 + 2) // 3
            appeared.add(nums[idx])
        return 0
