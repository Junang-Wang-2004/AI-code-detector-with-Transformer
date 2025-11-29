class C1(object):

    def minimumRecolors(self, a1, a2):
        """
        """
        v1 = a2
        v2 = 0
        for v3, v4 in enumerate(a1):
            v2 += int(a1[v3] == 'W')
            if v3 + 1 - a2 < 0:
                continue
            v1 = min(v1, v2)
            v2 -= int(a1[v3 + 1 - a2] == 'W')
        return v1
