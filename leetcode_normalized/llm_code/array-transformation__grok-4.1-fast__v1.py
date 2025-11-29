class C1:

    def transformArray(self, a1):
        while True:
            v1 = a1[:]
            v2 = False
            for v3 in range(1, len(a1) - 1):
                v4, v5, v6 = (a1[v3 - 1], a1[v3], a1[v3 + 1])
                if v4 > v5 and v5 < v6:
                    v1[v3] += 1
                    v2 = True
                elif v4 < v5 and v5 > v6:
                    v1[v3] -= 1
                    v2 = True
            a1 = v1
            if not v2:
                break
        return a1
