class C1:

    def findFarmland(self, a1):
        if not a1 or not a1[0]:
            return []
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = []
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] == 0:
                    continue
                if v4 > 0 and a1[v4 - 1][v5] == 1:
                    continue
                if v5 > 0 and a1[v4][v5 - 1] == 1:
                    continue
                v6 = v4
                while v6 + 1 < v1 and a1[v6 + 1][v5] == 1:
                    v6 += 1
                v7 = v5
                while v7 + 1 < v2 and a1[v4][v7 + 1] == 1:
                    v7 += 1
                v3.append([v4, v5, v6, v7])
        return v3
