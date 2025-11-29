class C1:

    def canPartitionGrid(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = sum((a1[r][c] for v4 in range(v1) for v5 in range(v2)))
        if v3 % 2 != 0:
            return False
        v6 = v3 // 2
        v7 = 0
        for v4 in range(v1):
            v8 = sum((a1[v4][v5] for v5 in range(v2)))
            v7 += v8
            if v7 == v6:
                return True
            if v7 > v6:
                break
        v7 = 0
        for v5 in range(v2):
            v9 = sum((a1[v4][v5] for v4 in range(v1)))
            v7 += v9
            if v7 == v6:
                return True
            if v7 > v6:
                break
        return False
