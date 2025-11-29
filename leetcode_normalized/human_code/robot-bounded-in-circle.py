class C1(object):

    def isRobotBounded(self, a1):
        """
        """
        v1 = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        v2, v3, v4 = (0, 0, 0)
        for v5 in a1:
            if v5 == 'R':
                v4 = (v4 + 1) % 4
            elif v5 == 'L':
                v4 = (v4 - 1) % 4
            else:
                v2 += v1[v4][0]
                v3 += v1[v4][1]
        return v2 == 0 and v3 == 0 or v4 > 0
