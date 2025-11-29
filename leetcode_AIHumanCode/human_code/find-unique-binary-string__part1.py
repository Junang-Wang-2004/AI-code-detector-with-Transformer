# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        """
        return "".join("01"[nums[i][i] == '0'] for i in range(len(nums)))


