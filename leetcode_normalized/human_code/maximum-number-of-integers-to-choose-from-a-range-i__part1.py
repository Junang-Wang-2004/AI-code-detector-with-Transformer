class C1(object):

    def maxCount(self, a1, a2, a3):
        """
        """
        v1 = min(int((-1 + (1 + 8 * a3)) ** 0.5 / 2), a2)
        v2 = (v1 + 1) * v1 // 2
        v3 = v1
        v4 = set(a1)
        for v5 in v4:
            if v5 <= v1:
                v2 -= v5
                v3 -= 1
        for v6 in range(v1 + 1, a2 + 1):
            if v6 in v4:
                continue
            if v2 + v6 > a3:
                break
            v2 += v6
            v3 += 1
        return v3
