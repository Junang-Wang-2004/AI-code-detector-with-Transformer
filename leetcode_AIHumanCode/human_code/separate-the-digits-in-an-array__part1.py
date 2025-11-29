# Time:  O(n * logr)
# Space: O(1)

# array
class Solution(object):
    def separateDigits(self, nums):
        """
        """
        result = []
        for x in reversed(nums):
            while x:
                result.append(x%10)
                x //= 10
        result.reverse()
        return result


