class C1(object):

    def sortPermutation(self, a1):
        """
        """
        v1 = -1
        for v2 in range(len(a1)):
            if a1[v2] == v2:
                continue
            v1 = v1 & v2 if v1 != -1 else v2
        return v1 if v1 != -1 else 0
