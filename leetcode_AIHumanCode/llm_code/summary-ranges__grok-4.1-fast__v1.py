class Solution:
    def summaryRanges(self, nums):
        result = []
        i = 0
        n = len(nums)
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            if i == j:
                result.append(f"{nums[i]}")
            else:
                result.append(f"{nums[i]}->{nums[j]}")
            i = j + 1
        return result
