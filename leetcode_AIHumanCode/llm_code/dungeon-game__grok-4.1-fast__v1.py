class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        need = [[0] * n for _ in range(m)]
        need[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        for j in range(n-2, -1, -1):
            need[m-1][j] = max(1, need[m-1][j+1] - dungeon[m-1][j])
        for i in range(m-2, -1, -1):
            need[i][n-1] = max(1, need[i+1][n-1] - dungeon[i][n-1])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                nxt = min(need[i+1][j], need[i][j+1])
                need[i][j] = max(1, nxt - dungeon[i][j])
        return need[0][0]
