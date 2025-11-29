class C1(object):

    def checkStraightLine(self, a1):
        """
        """
        v1, v2 = a1[:2]
        return all((v1[0] * v2[1] - v2[0] * v1[1] + v2[0] * k[1] - k[0] * v2[1] + k[0] * v1[1] - v1[0] * k[1] == 0 for v3 in a1))
