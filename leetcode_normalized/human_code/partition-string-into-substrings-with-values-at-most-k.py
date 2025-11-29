class C1(object):

    def minimumPartition(self, a1, a2):
        """
        """
        v1 = 1
        v2 = 0
        for v3 in a1:
            if int(v3) > a2:
                return -1
            if v2 * 10 + int(v3) > a2:
                v1 += 1
                v2 = 0
            v2 = v2 * 10 + int(v3)
        return v1
