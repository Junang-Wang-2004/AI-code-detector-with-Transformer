# Time:  O(n^2)
# Space: O(n)
# hash table
class Solution3(object):
    def sumCounts(self, nums):
        """
        """
        MOD = 10**9+7
        result = 0
        for i in range(len(nums)):
            lookup = set()
            for j in reversed(range(i+1)):
                lookup.add(nums[j])
                result = (result+len(lookup)**2) % MOD
        return result
