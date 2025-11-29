class C1(object):

    def transformArray(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            if v2 % 2:
                continue
            a1[v1] = 0
            v1 += 1
        for v3 in range(v1, len(a1)):
            a1[v3] = 1
        return a1
