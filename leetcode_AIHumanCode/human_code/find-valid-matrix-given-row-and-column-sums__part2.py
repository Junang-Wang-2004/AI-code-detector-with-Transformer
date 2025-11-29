# Time:  O(m * n)
# Space: O(1)
class Solution2(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        """
        matrix = [[0]*len(colSum) for _ in range(len(rowSum))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = min(rowSum[i], colSum[j])  # greedily used
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
