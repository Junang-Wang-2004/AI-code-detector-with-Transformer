class C1(object):

    def halvesAreAlike(self, a1):
        """
        """
        v1 = set('aeiouAEIOU')
        v2 = v3 = 0
        v4, v5 = (0, len(a1) - 1)
        while v4 < v5:
            v2 += a1[v4] in v1
            v3 += a1[v5] in v1
            v4 += 1
            v5 -= 1
        return v2 == v3
