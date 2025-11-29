class C1(object):

    def intersection(self, a1, a2):
        """
        """
        (a1.sort(), a2.sort())
        v1 = []
        v2, v3 = (0, 0)
        while v2 < len(a1) and v3 < len(a2):
            if a1[v2] < a2[v3]:
                v2 += 1
            elif a1[v2] > a2[v3]:
                v3 += 1
            else:
                if not v1 or v1[-1] != a1[v2]:
                    v1 += (a1[v2],)
                v2 += 1
                v3 += 1
        return v1
