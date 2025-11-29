class C1:

    def __init__(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        self.prefix = [[0] * (v2 + 1) for v3 in range(v1 + 1)]
        for v4 in range(v1):
            for v5 in range(v2):
                self.prefix[v4 + 1][v5 + 1] = a1[v4][v5] + self.prefix[v4][v5 + 1] + self.prefix[v4 + 1][v5] - self.prefix[v4][v5]

    def sumRegion(self, a1, a2, a3, a4):
        return self.prefix[a3 + 1][a4 + 1] + self.prefix[a1][a2] - self.prefix[a1][a4 + 1] - self.prefix[a3 + 1][a2]
