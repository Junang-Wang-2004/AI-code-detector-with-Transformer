# Time:  O(n + r)
# Space: O(n)

# hash table
class Solution(object):
    def findMissingElements(self, nums):
        """
        """
        lookup = set(nums)
        return [x for x in range(min(nums)+1, max(nums)) if x not in lookup]
