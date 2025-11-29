class C1(object):

    def countCollisions(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = 1
        for v4 in a1:
            if v4 == 'R':
                v2 += 1
            elif v4 == 'S' or (v2 or not v3):
                v1 += v2 + int(v4 == 'L')
                v2 = v3 = 0
        return v1
