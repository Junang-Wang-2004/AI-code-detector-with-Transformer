class C1(object):

    def firstBadVersion(self, a1):
        """
        """
        v1, v2 = (1, a1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) / 2
            if isBadVersion(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
