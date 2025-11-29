class C1:

    def __init__(self, a1):
        self.mat = a1
        self.rev_ops = []

    def updateSubrectangle(self, a1, a2, a3, a4, a5):
        self.rev_ops.append((a1, a2, a3, a4, a5))

    def getValue(self, a1, a2):
        v1 = len(self.rev_ops)
        for v2 in range(v1 - 1, -1, -1):
            v3, v4, v5, v6, v7 = self.rev_ops[v2]
            if v3 <= a1 <= v5 and v4 <= a2 <= v6:
                return v7
        return self.mat[a1][a2]
