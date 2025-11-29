class C1(object):

    def isToeplitzMatrix(self, a1):
        """
        """
        for v1, v2 in enumerate(a1):
            for v3, v4 in enumerate(v2):
                if not v1 or not v3:
                    continue
                if a1[v1 - 1][v3 - 1] != v4:
                    return False
        return True
