class C1(object):

    def canBeIncreasing(self, a1):
        """
        """
        v1 = False
        for v2 in range(1, len(a1)):
            if a1[v2] > a1[v2 - 1]:
                continue
            if v1:
                return False
            v1 = True
            if v2 >= 2 and a1[v2 - 2] > a1[v2]:
                a1[v2] = a1[v2 - 1]
        return True
