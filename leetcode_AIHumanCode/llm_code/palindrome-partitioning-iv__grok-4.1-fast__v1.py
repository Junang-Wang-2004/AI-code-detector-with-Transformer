class Solution:
    def checkPartitioning(self, s):
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                pal[i][i + 1] = True
        for lng in range(3, n + 1):
            for i in range(n - lng + 1):
                j = i + lng - 1
                if s[i] == s[j] and pal[i + 1][j - 1]:
                    pal[i][j] = True
        for a in range(1, n - 1):
            if not pal[0][a - 1]:
                continue
            for b in range(a + 1, n):
                if pal[a][b - 1] and pal[b][n - 1]:
                    return True
        return False
