class C1(object):

    def minSizeSubarray(self, a1, a2):
        v1 = len(a1)
        v2 = sum(a1)
        v3 = a2 // v2
        v4 = a2 % v2
        if v4 == 0:
            return v3 * v1
        v5 = a1 + a1
        v6 = [0]
        for v7 in v5:
            v6.append(v6[-1] + v7)
        v8 = {0: 0}
        v9 = float('inf')
        for v10 in range(1, 2 * v1 + 1):
            v11 = v6[v10]
            if v11 - v4 in v8:
                v12 = v10 - v8[v11 - v4]
                if v12 <= v1:
                    v9 = min(v9, v12)
            v8[v11] = v10
        return v3 * v1 + v9 if v9 != float('inf') else -1
