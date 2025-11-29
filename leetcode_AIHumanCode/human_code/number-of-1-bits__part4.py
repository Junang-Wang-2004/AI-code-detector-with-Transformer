# Time:  O(logn) = O(32)
# Space: O(1)
class Solution4(object):
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n: int) -> int:
        b="{0:b}".format(n)
        result=b.count("1")
        return result
