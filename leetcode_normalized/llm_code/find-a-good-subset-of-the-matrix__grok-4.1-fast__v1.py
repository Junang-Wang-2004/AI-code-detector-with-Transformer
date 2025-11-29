class C1(object):

    def goodSubsetofBinaryMatrix(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return []
        v2 = len(a1[0])
        v3 = {}
        for v4 in range(v1):
            v5 = 0
            for v6 in range(v2):
                if a1[v4][v6]:
                    v5 |= 1 << v6
            if v5 == 0:
                return [v4]
            for v7, v8 in v3.items():
                if v7 & v5 == 0:
                    return [v8, v4]
            v3[v5] = v4
        return []
