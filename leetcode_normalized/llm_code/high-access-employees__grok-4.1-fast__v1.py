class C1:

    def findHighAccessEmployees(self, a1):
        v1 = {}
        for v2, v3 in a1:
            v4 = int(v3[0:2])
            v5 = int(v3[2:4])
            v6 = v4 * 60 + v5
            if v2 not in v1:
                v1[v2] = []
            v1[v2].append(v6)
        v7 = []
        for v2, v8 in v1.items():
            v9 = sorted(v8)
            v10 = len(v9)
            if v10 >= 3:
                v11 = False
                for v12 in range(v10 - 2):
                    if v9[v12 + 2] - v9[v12] < 60:
                        v11 = True
                        break
                if v11:
                    v7.append(v2)
        return v7
