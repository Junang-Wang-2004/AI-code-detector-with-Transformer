class C1(object):

    def furthestDistanceFromOrigin(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 == 'L':
                v1 -= 1
            elif v3 == 'R':
                v1 += 1
            else:
                v2 += 1
        return abs(v1) + v2
