class C1(object):

    def totalStrength(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = [0] * (len(a1) + 1)
        for v4 in range(len(a1)):
            v2 = (v2 + a1[v4]) % v1
            v3[v4 + 1] = (v3[v4] + v2) % v1
        v5, v6 = ([-1], 0)
        for v4 in range(len(a1) + 1):
            while v5[-1] != -1 and (v4 == len(a1) or a1[v5[-1]] >= a1[v4]):
                v7, v8, v9 = (v5[-2] + 1, v5.pop(), v4 - 1)
                v6 = (v6 + a1[v8] * ((v8 - v7 + 1) * (v3[v9 + 1] - v3[v8]) - (v9 - v8 + 1) * (v3[v8] - v3[max(v7 - 1, 0)]))) % v1
            v5.append(v4)
        return v6
