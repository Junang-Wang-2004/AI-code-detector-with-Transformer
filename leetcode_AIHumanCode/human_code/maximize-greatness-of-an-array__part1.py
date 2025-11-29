# Time:  O(n)
# Space: O(n)

# freq table, contructive algorithms
class Solution(object):
    def maximizeGreatness(self, nums):
        """
        """
        return len(nums)-max(collections.Counter(nums).values())
  

