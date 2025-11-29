class C1(object):

    def matrixSumQueries(self, a1, a2):
        v1 = [False] * a1
        v2 = [False] * a1
        v3 = 0
        v4 = 0
        v5 = 0
        for v6, v7, v8 in reversed(a2):
            if v6 == 0:
                if v1[v7]:
                    continue
                v1[v7] = True
                v3 += 1
                v5 += v8 * (a1 - v4)
            else:
                if v2[v7]:
                    continue
                v2[v7] = True
                v4 += 1
                v5 += v8 * (a1 - v3)
        return v5
