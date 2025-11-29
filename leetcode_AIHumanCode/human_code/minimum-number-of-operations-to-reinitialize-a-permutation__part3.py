# Time:  O(n)
# Space: O(1)
class Solution3(object):
    def reinitializePermutation(self, n):
        """
        """
        result, i = 0, 1
        while not result or i != 1:  # find cycle length
            i = (i//2 if not i%2 else n//2+(i-1)//2)
            result += 1
        return result
