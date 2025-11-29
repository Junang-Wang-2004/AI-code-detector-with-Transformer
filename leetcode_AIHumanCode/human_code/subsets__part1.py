# Time:  O(n * 2^n)
# Space: O(1)

class Solution(object):
    def subsets(self, nums):
        """
        """
        nums.sort()
        result = [[]]
        for i in range(len(nums)):
            size = len(result)
            for j in range(size):
                result.append(list(result[j]))
                result[-1].append(nums[i])
        return result


