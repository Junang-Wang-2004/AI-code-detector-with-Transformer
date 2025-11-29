class C1(object):

    def countBinarySubstrings(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, 1)
        for v4 in range(1, len(a1)):
            if a1[v4 - 1] != a1[v4]:
                v1 += min(v2, v3)
                v2, v3 = (v3, 1)
            else:
                v3 += 1
        v1 += min(v2, v3)
        return v1
