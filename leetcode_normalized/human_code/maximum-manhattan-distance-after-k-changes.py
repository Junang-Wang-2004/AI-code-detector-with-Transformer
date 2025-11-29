class C1(object):

    def maxDistance(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        for v4, v5 in enumerate(a1, 1):
            if v5 == 'E':
                v2 += 1
            elif v5 == 'W':
                v2 -= 1
            elif v5 == 'N':
                v3 += 1
            elif v5 == 'S':
                v3 -= 1
            v1 = max(v1, min(abs(v2) + abs(v3) + 2 * a2, v4))
        return v1
