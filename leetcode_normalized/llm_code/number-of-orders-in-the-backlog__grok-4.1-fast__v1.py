class C1:

    def getNumberOfBacklogOrders(self, a1):
        v1 = 10 ** 9 + 7
        v2 = []
        v3 = []
        for v4, v5, v6 in a1:
            if v6 == 0:
                v2.append([v4, v5])
            else:
                v3.append([v4, v5])
        v2.sort(key=lambda x: x[0], reverse=True)
        v3.sort(key=lambda x: x[0])
        v7 = 0
        v8 = 0
        while v7 < len(v2) and v8 < len(v3):
            if v2[v7][0] >= v3[v8][0]:
                v9 = min(v2[v7][1], v3[v8][1])
                v2[v7][1] -= v9
                v3[v8][1] -= v9
                if v2[v7][1] == 0:
                    v7 += 1
                if v3[v8][1] == 0:
                    v8 += 1
            else:
                break
        v10 = 0
        for v11 in v2 + v3:
            v10 = (v10 + v11[1]) % v1
        return v10
