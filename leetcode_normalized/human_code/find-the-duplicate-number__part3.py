class C1(object):

    def findDuplicate(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            if a1[abs(v2) - 1] > 0:
                a1[abs(v2) - 1] *= -1
            else:
                v1 = abs(v2)
                break
        for v2 in a1:
            if a1[abs(v2) - 1] < 0:
                a1[abs(v2) - 1] *= -1
            else:
                break
        return v1
