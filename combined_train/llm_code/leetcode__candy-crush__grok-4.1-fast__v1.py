class C1:

    def candyCrush(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        while True:
            v3 = False
            for v4 in range(v1):
                for v5 in range(v2 - 2):
                    v6 = abs(a1[v4][v5])
                    if v6 > 0 and v6 == abs(a1[v4][v5 + 1]) and (v6 == abs(a1[v4][v5 + 2])):
                        a1[v4][v5] = a1[v4][v5 + 1] = a1[v4][v5 + 2] = -v6
                        v3 = True
            for v5 in range(v2):
                for v4 in range(v1 - 2):
                    v6 = abs(a1[v4][v5])
                    if v6 > 0 and v6 == abs(a1[v4 + 1][v5]) and (v6 == abs(a1[v4 + 2][v5])):
                        a1[v4][v5] = a1[v4 + 1][v5] = a1[v4 + 2][v5] = -v6
                        v3 = True
            if not v3:
                break
            for v5 in range(v2):
                v7 = [a1[v4][v5] for v4 in range(v1) if a1[v4][v5] > 0]
                v8 = v1 - len(v7)
                for v4 in range(v8):
                    a1[v4][v5] = 0
                for v9, v4 in enumerate(range(v8, v1)):
                    a1[v4][v5] = v7[v9]
        return a1
