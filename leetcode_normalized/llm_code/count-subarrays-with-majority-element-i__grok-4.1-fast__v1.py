class C1(object):

    def countMajoritySubarrays(self, a1, a2):
        v1 = len(a1)
        v2 = v1
        v3 = 2 * v1 + 1
        v4 = [0] * v3
        v5 = [0] * v3
        v6 = v2
        v4[v6] = 1
        v5[v6] = 1
        v7 = 0
        v8 = 0
        for v9 in a1:
            v7 += 1 if v9 == a2 else -1
            v10 = v7 + v2
            v4[v10] += 1
            v5[v10] = v5[v10 - 1] + v4[v10]
            v8 += v5[v10 - 1]
        return v8
