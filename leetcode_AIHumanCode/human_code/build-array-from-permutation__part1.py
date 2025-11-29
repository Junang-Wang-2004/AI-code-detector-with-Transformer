# Time:  O(n)
# Space: O(1)

# inplace solution
class Solution(object):
    def buildArray(self, nums):
        """
        """
        for i in range(len(nums)):
            prev, curr = i, nums[i]
            while curr >= 0 and curr != i:
                nums[prev], nums[curr] = ~nums[curr], ~nums[prev] if prev == i else nums[prev]
                prev, curr = curr, ~nums[prev]
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = ~nums[i]
        return nums


