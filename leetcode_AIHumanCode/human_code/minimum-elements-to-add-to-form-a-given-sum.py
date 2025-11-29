# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        """
        return (abs(sum(nums)-goal) + (limit-1))//limit
