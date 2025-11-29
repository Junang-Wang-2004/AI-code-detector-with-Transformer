# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def findErrorNums(self, nums):
        """
        """
        result = [0] * 2
        for i in nums:
            if nums[abs(i)-1] < 0:
                result[0] = abs(i)
            else:
                nums[abs(i)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                result[1] = i+1
            else:
                nums[i] *= -1
        return result


