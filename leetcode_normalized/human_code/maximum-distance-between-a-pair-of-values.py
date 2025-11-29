class C1(object):

    def maxDistance(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        while v2 < len(a1) and v3 < len(a2):
            if a1[v2] > a2[v3]:
                v2 += 1
            else:
                v1 = max(v1, v3 - v2)
                v3 += 1
        return v1
