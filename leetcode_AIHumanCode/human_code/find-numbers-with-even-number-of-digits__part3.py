# Time:  O(nlogm), n the length of nums, m is the max value of nums
# Space: O(logm)
class Solution3(object):
    def findNumbers(self, nums):
        """
        """
        return sum(len(str(n)) % 2 == 0 for n in nums)
