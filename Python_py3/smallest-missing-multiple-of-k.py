# Time:  O(n)
# Space: O(n)

# hash table
class Solution(object):
    def missingMultiple(self, nums, k):
        """
        """
        lookup = set(nums)
        for i in range(1, len(lookup)+1):
            if i*k not in lookup:
                return i*k
        return (len(lookup)+1)*k
