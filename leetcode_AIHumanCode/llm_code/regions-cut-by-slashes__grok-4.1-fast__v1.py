class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def link(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1


class Solution:
    def regionsBySlashes(self, grid):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        dsu = DSU(4 * rows * cols)

        def get_id(row, col, part):
            return row * (4 * cols) + col * 4 + part

        TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3

        # Connect vertically adjacent regions
        for row in range(1, rows):
            for col in range(cols):
                dsu.link(get_id(row - 1, col, BOTTOM), get_id(row, col, TOP))

        # Connect horizontally adjacent regions
        for row in range(rows):
            for col in range(1, cols):
                dsu.link(get_id(row, col - 1, RIGHT), get_id(row, col, LEFT))

        # Connect regions within each cell
        for row in range(rows):
            for col in range(cols):
                symbol = grid[row][col]
                if symbol != '/':
                    dsu.link(get_id(row, col, TOP), get_id(row, col, RIGHT))
                    dsu.link(get_id(row, col, BOTTOM), get_id(row, col, LEFT))
                if symbol != '\\':
                    dsu.link(get_id(row, col, LEFT), get_id(row, col, TOP))
                    dsu.link(get_id(row, col, RIGHT), get_id(row, col, BOTTOM))

        return dsu.components
