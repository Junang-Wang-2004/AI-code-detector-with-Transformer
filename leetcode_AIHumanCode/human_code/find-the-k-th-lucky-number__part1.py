# Time:  O(logn)
# Space: O(1)

# math, bitmasks
class Solution(object):
    def kthLuckyNumber(self, k):
        """
        """
        result = []
        k += 1
        while k != 1:
            result.append('7' if k&1 else '4')
            k >>= 1
        result.reverse()
        return "".join(result)


