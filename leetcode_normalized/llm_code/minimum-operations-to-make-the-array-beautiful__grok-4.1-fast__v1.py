class C1:

    def minOperations(self, a1):
        if not a1:
            return 0
        v1 = max(a1)
        if v1 == 1:
            return 0
        v2 = {a1[0]: 0}
        v3 = 2 * v1 - 1
        for v4 in range(1, len(a1)):
            v5 = a1[v4]
            v6 = {}
            for v7, v8 in v2.items():
                v9 = (v5 + v7 - 1) // v7
                v10 = v3 // v7
                for v11 in range(v9, v10 + 1):
                    v12 = v11 * v7
                    if v12 > v3:
                        break
                    v13 = v8 + v12 - v5
                    if v12 not in v6 or v13 < v6[v12]:
                        v6[v12] = v13
            v2 = v6
        return min(v2.values())
