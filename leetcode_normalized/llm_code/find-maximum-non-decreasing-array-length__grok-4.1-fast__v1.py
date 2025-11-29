class C1(object):

    def findMaximumLength(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [0] * (v1 + 1)
        v5 = 0
        for v3 in range(1, v1 + 1):
            while v5 + 1 < v3 and v2[v3] > 2 * v2[v5 + 1]:
                v5 += 1
            v4[v3] = v4[v5] + 1
        return v4[v1]
