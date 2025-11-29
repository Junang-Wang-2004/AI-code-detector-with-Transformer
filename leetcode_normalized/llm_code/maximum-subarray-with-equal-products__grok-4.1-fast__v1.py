class C1:

    def maxLength(self, a1):
        v1 = [[] for v2 in range(11)]
        for v3 in range(2, 11):
            if not v1[v3]:
                for v4 in range(v3, 11, v3):
                    v1[v4].append(v3)
        v5 = 0
        v6 = {}
        v7 = 0
        for v8 in range(len(a1)):
            v9 = a1[v8]
            for v10 in v1[v9]:
                v7 = max(v7, v6.get(v10, 0))
                v6[v10] = v8 + 1
            v5 = max(v5, v8 - v7 + 1)
        return v5
