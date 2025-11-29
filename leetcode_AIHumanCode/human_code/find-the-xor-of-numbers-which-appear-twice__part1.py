# Time:  O(n)
# Space: O(n)

# hash table
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        """
        return reduce(lambda x, y: x^y, nums, 0)^reduce(lambda x, y: x^y, set(nums), 0)


