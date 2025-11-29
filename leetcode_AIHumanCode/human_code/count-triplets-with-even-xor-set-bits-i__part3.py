# Time:  O(n^3 * logr), r = max(max(a), max(b), max(c))
# Space: O(1)
# brute force, bit manipulation
class Solution3(object):
    def tripletCount(self, a, b, c):
        """
        """
        def popcount(x):
            return bin(x).count('1')

        return sum(popcount(x^y^z)%2 == 0 for x in a for y in b for z in c)
