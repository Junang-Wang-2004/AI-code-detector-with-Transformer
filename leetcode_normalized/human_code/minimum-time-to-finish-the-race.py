class C1(object):

    def minimumFinishTime(self, a1, a2, a3):
        """
        """

        def ceil_log2(a1):
            return (a1 - 1).bit_length()
        v1 = [float('inf')] * ceil_log2(a2 + 1)
        for v2, v3 in a1:
            v4 = v5 = v2
            v6 = 0
            while v5 < a2 + v2:
                v1[v6] = min(v1[v6], v4)
                v5 *= v3
                v4 += v5
                v6 += 1
        v7 = [float('inf')] * a3
        for v8 in range(a3):
            v7[v8] = min(((v7[v8 - j - 1] + a2 if v8 - j - 1 >= 0 else 0) + v1[j] for v9 in range(min(v8 + 1, len(v1)))))
        return v7[-1]
