class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        path = [[r0, c0]]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col = r0, c0
        length = 1
        d = 0
        target = R * C
        while len(path) < target:
            for _ in range(2):
                dr, dc = dirs[d]
                for _ in range(length):
                    row += dr
                    col += dc
                    if 0 <= row < R and 0 <= col < C:
                        path.append([row, col])
                    if len(path) == target:
                        return path
                d = (d + 1) % 4
            length += 1
        return path
