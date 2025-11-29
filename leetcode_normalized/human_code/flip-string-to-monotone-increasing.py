class C1(object):

    def minFlipsMonoIncr(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v1 += int(v3 == '1')
            v2 = min(v1, v2 + int(v3 == '0'))
        return v2
