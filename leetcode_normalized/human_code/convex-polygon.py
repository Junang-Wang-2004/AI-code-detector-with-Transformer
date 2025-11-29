class C1(object):

    def isConvex(self, a1):
        """
        """

        def det(a1):
            return a1[0][0] * a1[1][1] - a1[0][1] * a1[1][0]
        v1, v2, v3 = (len(a1), 0, None)
        for v4 in range(len(a1)):
            v5 = [[a1[(v4 + j) % v1][0] - a1[v4][0], a1[(v4 + j) % v1][1] - a1[v4][1]] for v6 in (1, 2)]
            v3 = det(v5)
            if v3:
                if v3 * v2 < 0:
                    return False
                v2 = v3
        return True
