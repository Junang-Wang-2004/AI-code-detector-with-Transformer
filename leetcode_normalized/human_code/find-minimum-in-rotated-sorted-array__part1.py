class C1(object):

    def findMin(self, a1):
        """
        """
        v1, v2 = (0, len(a1))
        v3 = a1[-1]
        while v1 < v2:
            v4 = v1 + (v2 - v1) / 2
            if a1[v4] <= v3:
                v2 = v4
            else:
                v1 = v4 + 1
        return a1[v1]
