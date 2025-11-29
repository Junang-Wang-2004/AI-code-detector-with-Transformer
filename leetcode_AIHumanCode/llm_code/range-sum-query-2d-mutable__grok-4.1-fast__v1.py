class NumMatrix:
    def __init__(self, matrix):
        self.row_count = self.col_count = 0
        self.original_values = []
        self.fenwick_tree = []
        if not matrix or not matrix[0]:
            return
        self.row_count = len(matrix)
        self.col_count = len(matrix[0])
        self.original_values = [list(row) for row in matrix]
        self.fenwick_tree = [[0] * (self.col_count + 1) for _ in range(self.row_count + 1)]
        for x in range(self.row_count):
            for y in range(self.col_count):
                self._modify(x, y, self.original_values[x][y])

    def update(self, r, c, new_val):
        diff = new_val - self.original_values[r][c]
        self.original_values[r][c] = new_val
        if diff:
            self._modify(r, c, diff)

    def sumRegion(self, r1, c1, r2, c2):
        def prefix_sum(row, col):
            total = 0
            row += 1
            col += 1
            idx = row
            while idx > 0:
                jdx = col
                while jdx > 0:
                    total += self.fenwick_tree[idx][jdx]
                    jdx -= jdx & -jdx
                idx -= idx & -idx
            return total
        return (prefix_sum(r2, c2) - prefix_sum(r2, c1 - 1) -
                prefix_sum(r1 - 1, c2) + prefix_sum(r1 - 1, c1 - 1))

    def _modify(self, r, c, delta):
        idx = r + 1
        jdx = c + 1
        maxr = self.row_count
        maxc = self.col_count
        while idx <= maxr:
            curj = jdx
            while curj <= maxc:
                self.fenwick_tree[idx][curj] += delta
                curj += curj & -curj
            idx += idx & -idx
