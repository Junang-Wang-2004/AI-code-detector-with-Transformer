class C1(object):

    def canEat(self, a1, a2):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2, v3 in enumerate(a1):
            v1[v2 + 1] = v1[v2] + v3
        return [v1[t] // v3 < d + 1 <= v1[t + 1] // 1 for v4, v5, v3 in a2]
