# Time:  O(n^2)
# Space: O(n)
class Solution3(object):
    def rotateString(self, A, B):
        """
        """
        return len(A) == len(B) and B in A*2

