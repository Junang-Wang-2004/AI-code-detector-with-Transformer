class C1(object):

    def totalStrength(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = ([0] * (len(a1) + 1), [0] * (len(a1) + 1))
        for v4 in range(len(a1)):
            v2[v4 + 1] = (v2[v4] + a1[v4]) % v1
            v3[v4 + 1] = (v3[v4] + a1[v4] * (v4 + 1)) % v1
        v5, v6 = ([0] * (len(a1) + 1), [0] * (len(a1) + 1))
        for v4 in reversed(range(len(a1))):
            v5[v4] = (v5[v4 + 1] + a1[v4]) % v1
            v6[v4] = (v6[v4 + 1] + a1[v4] * (len(a1) - v4)) % v1
        v7, v8 = ([-1], 0)
        for v4 in range(len(a1) + 1):
            while v7[-1] != -1 and (v4 == len(a1) or a1[v7[-1]] >= a1[v4]):
                v9, v10, v11 = (v7[-2] + 1, v7.pop(), v4 - 1)
                v8 = (v8 + a1[v10] * ((v11 - v10 + 1) * (v3[v10 + 1] - v3[v9] - v9 * (v2[v10 + 1] - v2[v9])) + (v10 - v9 + 1) * (v6[v10 + 1] - v6[v11 + 1] - (len(a1) - (v11 + 1)) * (v5[v10 + 1] - v5[v11 + 1])))) % v1
            v7.append(v4)
        return v8
