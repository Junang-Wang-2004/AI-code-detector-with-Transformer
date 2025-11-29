class C1(object):

    def numberOfPairs(self, a1):
        v1 = {}
        for v2 in a1:
            if v2 in v1:
                v1[v2] += 1
            else:
                v1[v2] = 1
        v3 = 0
        for v4 in v1.values():
            v3 += v4 // 2
        v5 = len(a1) - 2 * v3
        return [v3, v5]
