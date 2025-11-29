class C1(object):

    def maxLengthBetweenEqualCharacters(self, a1):
        """
        """
        v1, v2 = (-1, {})
        for v3, v4 in enumerate(a1):
            v1 = max(v1, v3 - v2.setdefault(v4, v3) - 1)
        return v1
