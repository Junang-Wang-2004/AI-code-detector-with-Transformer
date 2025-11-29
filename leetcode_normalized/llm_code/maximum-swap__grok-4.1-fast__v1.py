class C1(object):

    def maximumSwap(self, a1):
        v1 = list(str(a1))
        v2 = len(v1)
        v3 = [-1] * 10
        for v4 in range(v2):
            v5 = int(v1[v4])
            v3[v5] = v4
        for v4 in range(v2):
            v6 = int(v1[v4])
            for v7 in range(9, v6, -1):
                v8 = v3[v7]
                if v8 > v4:
                    v1[v4], v1[v8] = (v1[v8], v1[v4])
                    return int(''.join(v1))
        return int(''.join(v1))
