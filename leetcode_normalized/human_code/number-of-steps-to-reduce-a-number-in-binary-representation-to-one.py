class C1(object):

    def numSteps(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in reversed(range(1, len(a1))):
            if int(a1[v3]) + v2 == 1:
                v2 = 1
                v1 += 2
            else:
                v1 += 1
        return v1 + v2
