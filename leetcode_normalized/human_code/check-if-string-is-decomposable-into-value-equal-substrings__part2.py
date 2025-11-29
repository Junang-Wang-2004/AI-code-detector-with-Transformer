class C1(object):

    def isDecomposable(self, a1):
        """
        """
        v1, v2 = (False, 0)
        while v2 < len(a1):
            v3 = 1
            for v4 in range(v2 + 1, min(v2 + 3, len(a1))):
                if a1[v4] != a1[v2]:
                    break
                v3 += 1
            if v3 < 2:
                return False
            if v3 == 2:
                if v1:
                    return False
                v1 = True
            v2 += v3
        return v1
