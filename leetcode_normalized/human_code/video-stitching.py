class C1(object):

    def videoStitching(self, a1, a2):
        """
        """
        if a2 == 0:
            return 0
        v1 = 1
        v2, v3 = (0, 0)
        a1.sort()
        for v4, v5 in a1:
            if v4 > v3:
                break
            elif v4 > v2:
                v2 = v3
                v1 += 1
            v3 = max(v3, v5)
            if v3 >= a2:
                return v1
        return -1
