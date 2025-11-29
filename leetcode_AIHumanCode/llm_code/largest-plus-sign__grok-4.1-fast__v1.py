class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        forbidden = set(map(tuple, mines))
        larm = [[0] * n for _ in range(n)]
        for r in range(n):
            streak = 0
            for c in range(n):
                streak = 0 if (r, c) in forbidden else streak + 1
                larm[r][c] = streak
        rarm = [[0] * n for _ in range(n)]
        for r in range(n):
            streak = 0
            for c in range(n - 1, -1, -1):
                streak = 0 if (r, c) in forbidden else streak + 1
                rarm[r][c] = streak
        uarm = [[0] * n for _ in range(n)]
        for c in range(n):
            streak = 0
            for r in range(n):
                streak = 0 if (r, c) in forbidden else streak + 1
                uarm[r][c] = streak
        darm = [[0] * n for _ in range(n)]
        for c in range(n):
            streak = 0
            for r in range(n - 1, -1, -1):
                streak = 0 if (r, c) in forbidden else streak + 1
                darm[r][c] = streak
        maximum = 0
        for r in range(n):
            for c in range(n):
                current = min(larm[r][c], rarm[r][c], uarm[r][c], darm[r][c])
                if current > maximum:
                    maximum = current
        return maximum
