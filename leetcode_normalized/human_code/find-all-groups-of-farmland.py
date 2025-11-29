class C1(object):

    def findFarmland(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                if a1[v2][v3] != 1:
                    continue
                v4, v5 = (v2, v3)
                while v4 + 1 < len(a1) and a1[v4 + 1][v3] == 1:
                    v4 += 1
                while v5 + 1 < len(a1[0]) and a1[v2][v5 + 1] == 1:
                    v5 += 1
                for v6 in range(v2, v4 + 1):
                    for v7 in range(v3, v5 + 1):
                        a1[v6][v7] = -1
                v1.append([v2, v3, v4, v5])
        return v1
