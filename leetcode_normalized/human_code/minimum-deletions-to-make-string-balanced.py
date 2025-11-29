class C1(object):

    def minimumDeletions(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 == 'b':
                v2 += 1
            elif v2:
                v2 -= 1
                v1 += 1
        return v1
