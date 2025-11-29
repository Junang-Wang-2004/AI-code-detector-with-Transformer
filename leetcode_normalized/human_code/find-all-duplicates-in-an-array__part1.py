class C1(object):

    def findDuplicates(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if a1[abs(v2) - 1] < 0:
                v1.append(abs(v2))
            else:
                a1[abs(v2) - 1] *= -1
        return v1
