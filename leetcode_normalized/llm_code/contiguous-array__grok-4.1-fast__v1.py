class C1:

    def findMaxLength(self, a1):
        v1 = 0
        v2 = 0
        v3 = {0: -1}
        for v4 in range(len(a1)):
            v2 += 2 * a1[v4] - 1
            if v2 not in v3:
                v3[v2] = v4
            v1 = max(v1, v4 - v3[v2])
        return v1
