class C1:

    def countServers(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [sum(r) for v4 in a1]
        v5 = [sum((a1[i][j] for v6 in range(v1))) for v7 in range(v2)]
        v8 = sum(v3)
        v9 = 0
        for v6 in range(v1):
            if v3[v6] == 1:
                for v7 in range(v2):
                    if a1[v6][v7]:
                        if v5[v7] == 1:
                            v9 += 1
                        break
        return v8 - v9
