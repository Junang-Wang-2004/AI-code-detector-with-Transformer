class C1(object):

    def findChampion(self, a1, a2):
        """
        """
        v1 = [False] * a1
        for v2, v3 in a2:
            v1[v3] = True
        v4 = -1
        for v2 in range(a1):
            if v1[v2]:
                continue
            if v4 != -1:
                return -1
            v4 = v2
        return v4
