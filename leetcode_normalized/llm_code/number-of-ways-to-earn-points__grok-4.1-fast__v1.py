class C1(object):

    def waysToReachTarget(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = [0] * (a1 + 1)
        v2[0] = 1
        for v3, v4 in a2:
            v5 = [0] * (a1 + 1)
            for v6 in range(v3 + 1):
                v7 = v6 * v4
                for v8 in range(a1 - v7 + 1):
                    v5[v8 + v7] = (v5[v8 + v7] + v2[v8]) % v1
            v2 = v5
        return v2[a1]
