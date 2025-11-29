# Time:  O(n + m)
# Space: O(n)
# hash table
class Solution2(object):
    def arrayChange(self, nums, operations):
        """
        """
        lookup = {x:i for i, x in enumerate(nums)}
        for x, y in operations:
            nums[lookup[x]] = y
            lookup[y] = lookup.pop(x)
        return nums
