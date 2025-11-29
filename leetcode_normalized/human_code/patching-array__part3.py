class C1(object):

    def minPatches(self, a1, a2):
        """
        """
        v1, v2, v3 = (0, 1, 0)
        while v2 <= a2:
            if v3 < len(a1) and a1[v3] <= v2:
                v2 += a1[v3]
                v3 += 1
            else:
                v2 += v2
                v1 += 1
        return v1
