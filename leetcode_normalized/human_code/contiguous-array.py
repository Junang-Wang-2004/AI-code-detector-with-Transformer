class C1(object):

    def findMaxLength(self, a1):
        """
        """
        v1, v2 = (0, 0)
        v3 = {0: -1}
        for v4, v5 in enumerate(a1):
            v2 += 1 if v5 == 1 else -1
            if v2 in v3:
                v1 = max(v1, v4 - v3[v2])
            else:
                v3[v2] = v4
        return v1
