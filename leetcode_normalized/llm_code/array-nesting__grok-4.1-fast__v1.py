class C1:

    def arrayNesting(self, a1):
        v1 = len(a1)
        v2 = [False] * v1
        v3 = 0
        for v4 in range(v1):
            if v2[v4]:
                continue
            v5 = 0
            v6 = v4
            while not v2[v6]:
                v2[v6] = True
                v6 = a1[v6]
                v5 += 1
            v3 = max(v3, v5)
        return v3
