class C1(object):

    def leftRigthDifference(self, a1):
        """
        """
        v1 = sum(a1)
        v2 = []
        v3 = 0
        for v4 in a1:
            v3 += v4
            v2.append(abs(v3 - v4 - (v1 - v3)))
        return v2
