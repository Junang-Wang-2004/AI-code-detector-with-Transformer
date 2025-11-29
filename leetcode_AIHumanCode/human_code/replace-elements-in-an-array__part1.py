# Time:  O(n + m)
# Space: O(n)

# hash table, optimized from solution2
class Solution(object):
    def arrayChange(self, nums, operations):
        """
        """
        lookup = {x:i for i, x in enumerate(nums)}
        for x, y in operations:
            lookup[y] = lookup.pop(x)
        for x, i in lookup.items():
            nums[i] = x
        return nums


