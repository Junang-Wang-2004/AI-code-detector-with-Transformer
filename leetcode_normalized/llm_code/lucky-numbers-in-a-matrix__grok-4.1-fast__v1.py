class C1:

    def luckyNumbers(self, a1):
        if not a1 or not a1[0]:
            return []
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [min(row) for v4 in a1]
        v5 = [float('-inf')] * v2
        for v6 in range(v2):
            for v7 in range(v1):
                v5[v6] = max(v5[v6], a1[v7][v6])
        v8 = []
        for v7 in range(v1):
            for v6 in range(v2):
                v9 = a1[v7][v6]
                if v9 == v3[v7] and v9 == v5[v6]:
                    v8.append(v9)
        return v8
