class C1(object):

    def longestMountain(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, 0)
        for v4 in range(1, len(a1)):
            if v3 and a1[v4 - 1] < a1[v4] or a1[v4 - 1] == a1[v4]:
                v2, v3 = (0, 0)
            v2 += a1[v4 - 1] < a1[v4]
            v3 += a1[v4 - 1] > a1[v4]
            if v2 and v3:
                v1 = max(v1, v2 + v3 + 1)
        return v1
