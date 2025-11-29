class C1(object):

    def isMonotonic(self, a1):
        """
        """
        v1, v2 = (False, False)
        for v3 in range(len(a1) - 1):
            if a1[v3] < a1[v3 + 1]:
                v1 = True
            elif a1[v3] > a1[v3 + 1]:
                v2 = True
        return not v1 or not v2
