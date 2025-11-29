# Time:  O(n^2)
# Space: O(n)
# DP solution.
class Solution2(object):
    def maximalRectangle(self, matrix):
        """
        """
        if not matrix:
            return 0

        result = 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0 for _ in range(n)]
        H = [0 for _ in range(n)]
        R = [n for _ in range(n)]

        for i in range(m):
            left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    L[j] = 0
                    H[j] = 0
                    R[j] = n
                    left = j + 1

            right = n
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j

        return result

