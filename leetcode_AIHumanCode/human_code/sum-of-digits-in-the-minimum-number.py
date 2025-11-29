# Time:  O(n * l)
# Space: O(l)

class Solution(object):
    def sumOfDigits(self, A):
        """
        """
        total = sum([int(c) for c in str(min(A))])
        return 1 if total % 2 == 0 else 0
