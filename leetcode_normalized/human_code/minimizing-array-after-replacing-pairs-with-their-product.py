class C1(object):

    def minArrayLength(self, a1, a2):
        """
        """
        if 0 in a1:
            return 1
        v1 = len(a1)
        v2 = a1[0]
        for v3 in range(1, len(a1)):
            if v2 * a1[v3] > a2:
                v2 = a1[v3]
            else:
                v2 *= a1[v3]
                v1 -= 1
        return v1
