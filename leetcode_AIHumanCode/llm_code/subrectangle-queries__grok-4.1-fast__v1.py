class SubrectangleQueries:
    def __init__(self, mat):
        self.mat = mat
        self.rev_ops = []

    def updateSubrectangle(self, rstart, cstart, rend, cend, val):
        self.rev_ops.append((rstart, cstart, rend, cend, val))

    def getValue(self, r, c):
        n = len(self.rev_ops)
        for idx in range(n - 1, -1, -1):
            rs, cs, re, ce, v = self.rev_ops[idx]
            if rs <= r <= re and cs <= c <= ce:
                return v
        return self.mat[r][c]
