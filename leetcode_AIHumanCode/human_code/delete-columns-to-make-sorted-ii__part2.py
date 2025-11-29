# Time:  O(n * m)
# Space: O(n)
class Solution2(object):
    def minDeletionSize(self, A):
        """
        """
        result = 0
        is_sorted = [False]*(len(A)-1)
        for j in range(len(A[0])):
            tmp = is_sorted[:]
            for i in range(len(A)-1):
                if A[i][j] > A[i+1][j] and tmp[i] == False:
                    result += 1
                    break
                if A[i][j] < A[i+1][j]:
                    tmp[i] = True
            else:
                is_sorted = tmp
        return result
