class C1(object):

    def splitArray(self, a1):
        """
        """
        if len(a1) < 7:
            return False
        v1 = [0] * len(a1)
        v1[0] = a1[0]
        for v2 in range(1, len(a1)):
            v1[v2] = v1[v2 - 1] + a1[v2]
        for v3 in range(3, len(a1) - 3):
            v4 = set()
            for v2 in range(1, v3 - 1):
                if v1[v2 - 1] == v1[v3 - 1] - v1[v2]:
                    v4.add(v1[v2 - 1])
            for v5 in range(v3 + 2, len(a1) - 1):
                if v1[-1] - v1[v5] == v1[v5 - 1] - v1[v3] and v1[v5 - 1] - v1[v3] in v4:
                    return True
        return False
