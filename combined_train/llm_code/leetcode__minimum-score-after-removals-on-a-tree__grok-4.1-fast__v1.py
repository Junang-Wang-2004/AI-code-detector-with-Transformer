class C1:

    def minimumScore(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = 0
        for v7 in a1:
            v6 ^= v7
        v8 = 10 ** 18

        def traverse(a1, a2, a3):
            v1 = a1[a1]
            for v2 in v2[a1]:
                if v2 != a2:
                    v3 = traverse(v2, a1, a3)
                    v1 ^= v3
            a3.append(v1)
            return v1
        for v9, v10 in a2:
            v11 = []
            traverse(v9, v10, v11)
            v12 = []
            traverse(v10, v9, v12)
            for v13 in (v11, v12):
                if not v13:
                    continue
                v14 = v13.pop()
                for v15 in v13:
                    v16 = v6 ^ v14
                    v17 = v15
                    v18 = v14 ^ v15
                    v19 = max(v16, v17, v18)
                    v20 = min(v16, v17, v18)
                    v8 = min(v8, v19 - v20)
        return v8
