# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        """
        a, curr, base = 0, n, 1
        while curr: 
            if curr % 10 == 0 or (curr % 10 == 1 and curr != 1):
                a += base
                curr -= 10  # carry
            a += base
            base *= 10
            curr //= 10
        return [a, n-a]


