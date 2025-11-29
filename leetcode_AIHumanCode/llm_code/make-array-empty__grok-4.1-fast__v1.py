class Solution:
    def countOperationsToEmptyArray(self, nums):
        n = len(nums)
        order = sorted(range(n), key=nums.__getitem__)
        ans = n
        for i in range(n - 1):
            if order[i] > order[i + 1]:
                ans += n - i - 1
        return ans
