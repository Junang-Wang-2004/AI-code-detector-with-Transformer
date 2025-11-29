class C1(object):

    def numberOfBeams(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            v4 = v3.count('1')
            if not v4:
                continue
            v1 += v2 * v4
            v2 = v4
        return v1
