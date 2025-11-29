class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        arena = [[0] * n for _ in range(m)]
        for r, c in guards:
            arena[r][c] = 2
        for r, c in walls:
            arena[r][c] = 1

        # Horizontal scans
        for i in range(m):
            # Rightward rays
            scanning = False
            for j in range(n):
                if arena[i][j] == 1 or arena[i][j] == 2:
                    scanning = arena[i][j] == 2
                elif arena[i][j] == 0 and scanning:
                    arena[i][j] = 3
            # Leftward rays
            scanning = False
            for j in range(n - 1, -1, -1):
                if arena[i][j] == 1 or arena[i][j] == 2:
                    scanning = arena[i][j] == 2
                elif arena[i][j] == 0 and scanning:
                    arena[i][j] = 3

        # Vertical scans
        for j in range(n):
            # Downward rays
            scanning = False
            for i in range(m):
                if arena[i][j] == 1 or arena[i][j] == 2:
                    scanning = arena[i][j] == 2
                elif arena[i][j] == 0 and scanning:
                    arena[i][j] = 3
            # Upward rays
            scanning = False
            for i in range(m - 1, -1, -1):
                if arena[i][j] == 1 or arena[i][j] == 2:
                    scanning = arena[i][j] == 2
                elif arena[i][j] == 0 and scanning:
                    arena[i][j] = 3

        return sum(row.count(0) for row in arena)
