class C1(object):

    def countSubarrays(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(1, v1 + 1):
            v2[v3] = v2[v3 - 1] + a1[v3 - 1]
        v4 = 0
        for v5 in range(v1):
            v6, v7 = (0, v5 + 1)
            while v6 < v7:
                v8 = (v6 + v7) // 2
                v9 = v2[v5 + 1] - v2[v8]
                v10 = v5 - v8 + 1
                if v9 * v10 < a2:
                    v7 = v8
                else:
                    v6 = v8 + 1
            v11 = v6
            v4 += v5 - v11 + 1
        return v4
