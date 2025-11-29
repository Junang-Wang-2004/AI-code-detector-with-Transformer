class C1:

    def minimumLengthEncoding(self, a1):
        v1 = list(set(a1))
        v2 = {}
        v3 = []
        for v4 in v1:
            v5 = v2
            for v6 in reversed(v4):
                if v6 not in v5:
                    v5[v6] = {}
                v5 = v5[v6]
            v3.append(v5)
        return sum((len(v4) + 1 for v4, v7 in zip(v1, v3) if not v7))
