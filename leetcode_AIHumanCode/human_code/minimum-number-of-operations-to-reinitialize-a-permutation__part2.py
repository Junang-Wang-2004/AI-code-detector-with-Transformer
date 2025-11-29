# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def reinitializePermutation(self, n):
        """
        """
        if n == 2:
            return 1
        result, i = 0, 1
        while not result or i != 1:
            i = (i*2)%(n-1)
            result += 1
        return result


