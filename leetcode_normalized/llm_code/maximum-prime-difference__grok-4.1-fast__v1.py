class C1:

    def maximumPrimeDifference(self, a1):
        v1 = 100
        v2 = [True] * (v1 + 1)
        v2[0] = v2[1] = False
        for v3 in range(2, int(v1 ** 0.5) + 1):
            if v2[v3]:
                for v4 in range(v3 * v3, v1 + 1, v3):
                    v2[v4] = False
        v5 = -1
        v6 = -1
        for v7 in range(len(a1)):
            v8 = a1[v7]
            if v8 <= v1 and v2[v8]:
                if v5 == -1:
                    v5 = v7
                v6 = v7
        return v6 - v5
