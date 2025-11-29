class C1:

    def checkIfPrerequisite(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
        v5 = [None] * a1
        for v6 in range(a1):
            v7 = set([v6])
            v8 = [v6]
            v9 = 0
            while v9 < len(v8):
                v10 = v8[v9]
                v9 += 1
                for v11 in v1[v10]:
                    if v11 not in v7:
                        v7.add(v11)
                        v8.append(v11)
            v5[v6] = v7
        v12 = []
        for v13, v14 in a3:
            v12.append(v14 in v5[v13])
        return v12
