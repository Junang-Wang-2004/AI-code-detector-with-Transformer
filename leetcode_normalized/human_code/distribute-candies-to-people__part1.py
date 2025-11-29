class C1(object):

    def distributeCandies(self, a1, a2):
        """
        """
        v1 = int((2 * a1 + 0.25) ** 0.5 - 0.5)
        v2 = a1 - (v1 + 1) * v1 // 2
        v3, v4 = divmod(v1, a2)
        v5 = [0] * a2
        for v6 in range(a2):
            v5[v6] = (v6 + 1) * (v3 + 1) + v3 * (v3 + 1) // 2 * a2 if v6 < v4 else (v6 + 1) * v3 + (v3 - 1) * v3 // 2 * a2
        v5[v4] += v2
        return v5
