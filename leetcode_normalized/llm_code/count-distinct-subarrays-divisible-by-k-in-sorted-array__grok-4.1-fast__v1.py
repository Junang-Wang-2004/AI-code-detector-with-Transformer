class C1(object):

    def numGoodSubarrays(self, a1, a2):
        v1 = {0: 1}
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = len(a1)
        while v4 < v5:
            v6 = a1[v4]
            v7 = 0
            v8 = v4
            while v8 < v5 and a1[v8] == v6:
                v7 = (v7 + v6) % a2
                v9 = (v3 + v7) % a2
                v2 += v1.get(v9, 0)
                v8 += 1
            v7 = 0
            v10 = v8 - v4
            for v11 in range(v10):
                v7 = (v7 + v6) % a2
                v9 = (v3 + v7) % a2
                v1[v9] = v1.get(v9, 0) + 1
            v3 = (v3 + v7) % a2
            v4 = v8
        return v2
