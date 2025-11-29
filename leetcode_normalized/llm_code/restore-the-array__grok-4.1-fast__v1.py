class C1(object):

    def numberOfArrays(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = len(str(a2))
        v4 = [0] * (v2 + 1)
        v4[v2] = 1
        for v5 in range(v2 - 1, -1, -1):
            if a1[v5] == '0':
                continue
            v6 = 0
            for v7 in range(v5, min(v5 + v3, v2)):
                v6 = v6 * 10 + int(a1[v7])
                if v6 > a2:
                    break
                v4[v5] = (v4[v5] + v4[v7 + 1]) % v1
        return v4[0]
