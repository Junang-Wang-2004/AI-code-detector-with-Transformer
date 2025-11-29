class C1(object):

    def findUnsortedSubarray(self, a1):
        """
        """
        v1 = sorted(a1)
        v2, v3 = (0, len(a1) - 1)
        while a1[v2] == v1[v2] or a1[v3] == v1[v3]:
            if v3 - v2 <= 1:
                return 0
            if a1[v2] == v1[v2]:
                v2 += 1
            if a1[v3] == v1[v3]:
                v3 -= 1
        return v3 - v2 + 1
