# Time:  O(n * l)
# Space: O(1)

class Solution(object):
    def minDeletionSize(self, A):
        """
        """
        result = 0
        for c in range(len(A[0])):
            for r in range(1, len(A)):
                if A[r-1][c] > A[r][c]:
                    result += 1
                    break
        return result


