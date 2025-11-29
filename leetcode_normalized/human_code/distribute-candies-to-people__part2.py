class C1(object):

    def distributeCandies(self, a1, a2):
        """
        """
        v1, v2 = (1, a1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not v3 <= a1 * 2 // (v3 + 1):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        v4 = v2
        v5 = a1 - (v4 + 1) * v4 // 2
        v6, v7 = divmod(v4, a2)
        v8 = [0] * a2
        for v9 in range(a2):
            v8[v9] = (v9 + 1) * (v6 + 1) + v6 * (v6 + 1) // 2 * a2 if v9 < v7 else (v9 + 1) * v6 + (v6 - 1) * v6 // 2 * a2
        v8[v7] += v5
        return v8
