# Time:  O(n * l)
# Space: O(n)

class Solution(object):
    def minDeletionSize(self, A):
        """
        """
        result = 0
        unsorted = set(range(len(A)-1))
        for j in range(len(A[0])):
            if any(A[i][j] > A[i+1][j] for i in unsorted):
                result += 1
            else:
                unsorted -= set(i for i in unsorted if A[i][j] < A[i+1][j])
        return result


