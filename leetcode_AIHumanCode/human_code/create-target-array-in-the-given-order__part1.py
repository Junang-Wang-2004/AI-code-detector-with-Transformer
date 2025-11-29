# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        """
        for i in range(len(nums)):
            for j in range(i):
                if index[j] >= index[i]:
                    index[j] += 1
        result = [0]*(len(nums))
        for i in range(len(nums)):
            result[index[i]] = nums[i]
        return result


