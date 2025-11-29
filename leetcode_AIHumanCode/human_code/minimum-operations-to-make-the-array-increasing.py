# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minOperations(self, nums):
        """
        """
        result = prev = 0
        for curr in nums:
            if prev < curr:
                prev = curr
                continue
            prev += 1
            result += prev-curr                
        return result
