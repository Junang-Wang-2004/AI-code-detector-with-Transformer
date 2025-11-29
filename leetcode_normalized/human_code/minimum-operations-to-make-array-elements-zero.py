class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = 0
        for v2, v3 in a1:
            v4 = 0
            v5 = v6 = 1
            while v5 <= v3:
                v7, v8 = (max(v2, v5), min(v3, 4 * v5 - 1))
                if v7 <= v8:
                    v4 += v6 * (v8 - v7 + 1)
                v6 += 1
                v5 *= 4
            v1 += (v4 + 1) // 2
        return v1
