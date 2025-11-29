class C1:

    def kWeakestRows(self, a1, a2):
        v1 = []
        for v2, v3 in enumerate(a1):
            v4 = 0
            for v5 in v3:
                if v5 == 0:
                    break
                v4 += 1
            v1.append((v4, v2))
        v1.sort()
        return [v2 for v6, v2 in v1[:a2]]
