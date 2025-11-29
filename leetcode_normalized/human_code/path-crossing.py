class C1(object):

    def isPathCrossing(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = {(0, 0)}
        for v4 in a1:
            if v4 == 'E':
                v1 += 1
            elif v4 == 'W':
                v1 -= 1
            elif v4 == 'N':
                v2 += 1
            elif v4 == 'S':
                v2 -= 1
            if (v1, v2) in v3:
                return True
            v3.add((v1, v2))
        return False
