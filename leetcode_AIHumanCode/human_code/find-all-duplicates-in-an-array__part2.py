# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def findDuplicates(self, nums):
        """
        """
        result = []
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1

        for i in range(len(nums)):
            if i != nums[i]-1:
                result.append(nums[i])
        return result


