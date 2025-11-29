# Time:  O(n * l + llogl), n = len(nums), l = len(nums[0])
# Space: O(l)
# hash table, sort
class Solution3(object):
    def intersection(self, nums):
        """
        """
        result = set(nums[0])
        for i in range(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return sorted(result)
