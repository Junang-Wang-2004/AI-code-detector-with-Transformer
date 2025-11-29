class C1(object):

    def maxSum(self, a1, a2):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = max(a1)
        v3 = 0
        v4 = 1
        while v4 <= v2:
            v3 += 1
            v4 <<= 1
        v5 = [0] * v3
        for v6 in a1:
            v7 = 0
            v8 = v6
            while v8 > 0:
                if v8 & 1:
                    v5[v7] += 1
                v7 += 1
                v8 >>= 1
        v9 = 0
        for v10 in range(1, a2 + 1):
            v11 = 0
            for v7 in range(v3):
                if v5[v7] >= v10:
                    v11 += 1 << v7
            v9 = (v9 + v11 * v11) % v1
        return v9
