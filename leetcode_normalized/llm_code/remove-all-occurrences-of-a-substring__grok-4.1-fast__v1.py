class C1(object):

    def removeOccurrences(self, a1, a2):
        v1 = len(a2)
        v2 = [0] * v1
        v3 = 0
        v4 = 1
        while v4 < v1:
            if a2[v4] == a2[v3]:
                v3 += 1
                v2[v4] = v3
                v4 += 1
            elif v3 != 0:
                v3 = v2[v3 - 1]
            else:
                v2[v4] = 0
                v4 += 1
        v5 = []
        v6 = []
        v7 = 0
        for v8 in a1:
            v9 = v7
            while v9 > 0 and v8 != a2[v9]:
                v9 = v2[v9 - 1]
            if v8 == a2[v9]:
                v9 += 1
            v7 = v9
            v5.append(v8)
            v6.append(v7)
            if v7 == v1:
                del v5[-v1:]
                del v6[-v1:]
                v7 = v6[-1] if v6 else 0
        return ''.join(v5)
