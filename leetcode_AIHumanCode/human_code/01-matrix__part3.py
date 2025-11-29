# Time:  O(m * n)
# Space: O(m * n)
import collections


class Solution3(object):
    def updateMatrix(self, matrix):
        """
        """
        queue = collections.deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = float("inf")

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            cell = queue.popleft()
            for dir in dirs:
                i, j = cell[0]+dir[0], cell[1]+dir[1]
                if not (0 <= i < len(matrix) and
                        0 <= j < len(matrix[0]) and
                        matrix[i][j] > matrix[cell[0]][cell[1]]+1):
                    continue
                queue.append((i, j))
                matrix[i][j] = matrix[cell[0]][cell[1]]+1

        return matrix
