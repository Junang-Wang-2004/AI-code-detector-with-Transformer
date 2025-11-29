class C1(object):

    def longestSubarray(self, a1, a2):
        v1 = {}
        v2 = 0
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            v6 = a1[v5]
            v1[v6] = v1.get(v6, 0) + 1
            if v1[v6] == 2:
                v2 += 1
            while v2 > a2:
                v7 = a1[v3]
                if v1[v7] == 2:
                    v2 -= 1
                v1[v7] -= 1
                if v1[v7] == 0:
                    del v1[v7]
                v3 += 1
            v4 = max(v4, v5 - v3 + 1)
        return v4
