class neighborSum:
    def __init__(self, grid):
        self.board = grid
        rows = len(grid)
        cols = len(grid[0])
        self.side_sums = {}
        self.angle_sums = {}
        side_dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        angle_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for r in range(rows):
            for c in range(cols):
                num = self.board[r][c]
                side_total = 0
                for dr, dc in side_dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        side_total += self.board[nr][nc]
                self.side_sums[num] = side_total
                angle_total = 0
                for dr, dc in angle_dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        angle_total += self.board[nr][nc]
                self.angle_sums[num] = angle_total

    def adjacentSum(self, num):
        return self.side_sums.get(num, 0)

    def diagonalSum(self, num):
        return self.angle_sums.get(num, 0)
