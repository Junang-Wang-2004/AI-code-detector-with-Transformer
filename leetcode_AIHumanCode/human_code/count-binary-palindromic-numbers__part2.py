# Time:  O(logn)
# Space: O(logn)
# bitmasks, combinatorics
class Solution2(object):
    def countBinaryPalindromes(self, n):
        """
        """
        s = list(map(int, bin(n)[2:]))
        l = len(s)//2
        return ((1<<l)-1)+(n>>l)+int(s[:len(s)-l]+s[:l][::-1] <= s)
