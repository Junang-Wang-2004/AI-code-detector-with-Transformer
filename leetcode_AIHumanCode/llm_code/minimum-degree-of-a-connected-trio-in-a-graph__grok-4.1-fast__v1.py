class Solution(object):
    def minTrioDegree(self, n, edges):
        matrix = [[False] * (n + 1) for _ in range(n + 1)]
        counts = [0] * (n + 1)
        for x, y in edges:
            matrix[x][y] = True
            matrix[y][x] = True
            counts[x] += 1
            counts[y] += 1
        minimum = float('inf')
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if not matrix[a][b]:
                    continue
                for c in range(b + 1, n + 1):
                    if matrix[a][c] and matrix[b][c]:
                        minimum = min(minimum, counts[a] + counts[b] + counts[c] - 6)
        return minimum if minimum != float('inf') else -1
