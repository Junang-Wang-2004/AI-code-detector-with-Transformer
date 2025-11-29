# Time:  O(nlogr), r = max(nums)
# Space: O(n)
# hash table   
class Solution2(object):
    def countDistinctIntegers(self, nums):
        """
        """
        return len({y for x in nums for y in (x, int(str(x)[::-1]))})
