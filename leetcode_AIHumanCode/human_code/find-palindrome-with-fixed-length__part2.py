# Time:  O(n * l)
# Space: O(l)
# math
class Solution2(object):
    def kthPalindrome(self, queries, intLength):
        """
        """
        def f(l, x):
            if 10**((l-1)//2)+(x-1) > 10**((l+1)//2)-1:
                return -1
            s = str(10**((l-1)//2)+(x-1))
            return int(s+s[::-1][l%2:])

        return [f(intLength, x) for x in queries]
