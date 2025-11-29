class C1(object):

    def maxFont(self, a1, a2, a3, a4, a5):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1

        def fits(a1):
            v1 = a4[a1]
            if a5.getHeight(v1) > a3:
                return False
            v2 = 0
            for v3, v4 in v1.items():
                v2 += v4 * a5.getWidth(v1, v3)
            return v2 <= a2
        v3, v4 = (0, len(a4) - 1)
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if fits(v5):
                v3 = v5 + 1
            else:
                v4 = v5 - 1
        return a4[v4] if v4 >= 0 else -1
