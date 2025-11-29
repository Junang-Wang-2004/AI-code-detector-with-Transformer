class C1(object):

    def bowlSubarrays(self, a1):
        v1 = len(a1)
        v2 = [1] * v1
        for v3 in range(1, v1):
            if a1[v3 - 1] > a1[v3]:
                v2[v3] = v2[v3 - 1] + 1
        v4 = [1] * v1
        for v3 in range(v1 - 2, -1, -1):
            if a1[v3] < a1[v3 + 1]:
                v4[v3] = v4[v3 + 1] + 1
        v5 = 0
        for v3 in range(v1):
            v6 = v2[v3] - 1
            v7 = v4[v3] - 1
            if v6 > 0 and v7 > 0:
                v5 += v6 * v7
        return v5
