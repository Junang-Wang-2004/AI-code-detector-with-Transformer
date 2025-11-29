# Time:  O(n * l + r), n = len(nums), l = len(nums[0]), r = max(nums)-min(nums)
# Space: O(l)
# hash table, counting sort
class Solution2(object):
    def intersection(self, nums):
        """
        """
        result = set(nums[0])
        for i in range(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return [i for i in range(min(result), max(result)+1) if i in result] if result else []


