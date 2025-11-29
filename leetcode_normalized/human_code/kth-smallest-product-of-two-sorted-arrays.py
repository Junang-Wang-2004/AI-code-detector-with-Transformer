class C1(object):

    def kthSmallestProduct(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4, a5):
            v1 = 0
            v2, v3 = (0, len(a2) - 1)
            v4 = reversed if a5 >= 0 else lambda x: x
            for v5 in v4(range(a4)):
                while v2 < len(a2) and a1[v5] * a2[v2] > a5:
                    v2 += 1
                v1 += len(a2) - 1 - v2 + 1
            v4 = (lambda x: x) if a5 >= 0 else reversed
            for v5 in v4(range(a4, len(a1))):
                if a1[v5] == 0:
                    if a5 >= 0:
                        v1 += len(a2)
                    continue
                while v3 >= 0 and a1[v5] * a2[v3] > a5:
                    v3 -= 1
                v1 += v3 - 0 + 1
            return v1 >= a3
        v1 = sum((x < 0 for v2 in a1))
        v3 = min((a1[i] * a2[j] for v4 in (0, -1) for v5 in (0, -1)))
        v6 = max((a1[v4] * a2[v5] for v4 in (0, -1) for v5 in (0, -1)))
        while v3 <= v6:
            v7 = v3 + (v6 - v3) // 2
            if check(a1, a2, a3, v1, v7):
                v6 = v7 - 1
            else:
                v3 = v7 + 1
        return v3
