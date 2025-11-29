class C1(object):

    def maxProduct(self, a1):
        """
        """

        def palindromic_subsequence_length(a1, a2):
            v1 = 0
            v2, v3 = (0, len(a1) - 1)
            v4, v5 = (1 << v2, 1 << v3)
            while v2 <= v3:
                if a2 & v4 == 0:
                    v2, v4 = (v2 + 1, v4 << 1)
                elif a2 & v5 == 0:
                    v3, v5 = (v3 - 1, v5 >> 1)
                elif a1[v2] == a1[v3]:
                    v1 += 1 if v2 == v3 else 2
                    v2, v4 = (v2 + 1, v4 << 1)
                    v3, v5 = (v3 - 1, v5 >> 1)
                else:
                    return 0
            return v1
        v1 = [palindromic_subsequence_length(a1, mask) for v2 in range(1 << len(a1))]
        v3 = 0
        for v2 in range(len(v1)):
            if v1[v2] * (len(a1) - v1[v2]) <= v3:
                continue
            v4 = v5 = len(v1) - 1 ^ v2
            while v4:
                v3 = max(v3, v1[v2] * v1[v4])
                v4 = v4 - 1 & v5
        return v3
