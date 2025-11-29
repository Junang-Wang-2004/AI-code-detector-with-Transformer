class C1(object):

    def judgeCircle(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            if v3 == 'U':
                v1 += 1
            elif v3 == 'D':
                v1 -= 1
            elif v3 == 'R':
                v2 += 1
            elif v3 == 'L':
                v2 -= 1
        return v1 == 0 and v2 == 0
