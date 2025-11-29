# Time:  O(n)
# Space: O(n)

# hash table
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        """
        lookup = set(nums)
        return sum((x-diff in lookup) and (x-2*diff in lookup) for x in nums)

    
