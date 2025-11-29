class C1(object):

    def isDecomposable(self, a1):
        """
        """
        v1, v2 = (False, 0)
        for v3, v4 in enumerate(a1):
            if not v2 or v4 != a1[v3 - 1]:
                if v2:
                    return False
                v2 = 1
                continue
            v2 += 1
            if v2 == 2:
                if v3 == len(a1) - 1 or a1[v3] != a1[v3 + 1]:
                    if v1:
                        return False
                    v1, v2 = (True, 0)
            elif v2 == 3:
                v2 = 0
        return v1
