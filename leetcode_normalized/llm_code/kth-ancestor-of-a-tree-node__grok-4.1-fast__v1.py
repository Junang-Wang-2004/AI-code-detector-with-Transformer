class C1:

    def __init__(self, a1, a2):
        v1 = 20
        self.jump = [[-1] * v1 for v2 in range(a1)]
        for v3 in range(a1):
            if a2[v3] != -1:
                self.jump[v3][0] = a2[v3]
        for v4 in range(1, v1):
            for v3 in range(a1):
                v5 = self.jump[v3][v4 - 1]
                if v5 != -1:
                    self.jump[v3][v4] = self.jump[v5][v4 - 1]

    def getKthAncestor(self, a1, a2):
        for v1 in range(20):
            if a2 & 1 << v1:
                if self.jump[a1][v1] == -1:
                    return -1
                a1 = self.jump[a1][v1]
        return a1
