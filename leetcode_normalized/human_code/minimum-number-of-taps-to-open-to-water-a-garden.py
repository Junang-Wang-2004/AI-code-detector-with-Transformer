class C1(object):

    def minTaps(self, a1, a2):
        """
        """

        def jump_game(a1):
            v1, v2, v3 = (0, 0, 0)
            for v4, v5 in enumerate(a1):
                if v4 > v2:
                    return -1
                if v4 > v3:
                    v3 = v2
                    v1 += 1
                v2 = max(v2, v4 + v5)
            return v1
        v1 = [0] * (a1 + 1)
        for v2, v3 in enumerate(a2):
            v4, v5 = (max(v2 - v3, 0), min(v2 + v3, a1))
            v1[v4] = max(v1[v4], v5 - v4)
        return jump_game(v1)
