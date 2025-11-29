class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i] - 1
            if 1 <= nums[i] <= n and nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        return [j + 1 for j in range(n) if nums[j] != j + 1]
