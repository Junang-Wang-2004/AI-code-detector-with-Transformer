class C1:

    def maximumSetSize(self, a1, a2):
        v1 = set(a1)
        v2 = set(a2)
        v3 = len(v1.difference(v2))
        v4 = len(v2.difference(v1))
        v5 = len(v1.intersection(v2))
        v6 = len(a1) // 2
        v7 = min(v3, v6)
        v8 = min(v4, v6)
        v9 = v6 - v7
        v10 = v6 - v8
        v11 = min(v5, v9 + v10)
        return v7 + v8 + v11
