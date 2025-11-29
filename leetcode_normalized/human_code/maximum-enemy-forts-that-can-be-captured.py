class C1(object):

    def captureForts(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if not a1[v3]:
                continue
            if a1[v3] == -a1[v2]:
                v1 = max(v1, v3 - v2 - 1)
            v2 = v3
        return v1
