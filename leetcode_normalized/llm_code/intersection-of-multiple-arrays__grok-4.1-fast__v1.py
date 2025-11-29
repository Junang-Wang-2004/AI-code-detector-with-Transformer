class C1:

    def intersection(self, a1):
        if not a1:
            return []
        v1 = 1000
        v2 = [0] * (v1 + 1)
        for v3 in a1:
            v4 = set(v3)
            for v5 in v4:
                v2[v5] += 1
        v6 = []
        v7 = len(a1)
        for v8 in range(1, v1 + 1):
            if v2[v8] == v7:
                v6.append(v8)
        return v6
