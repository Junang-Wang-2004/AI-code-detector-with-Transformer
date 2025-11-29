class C1(object):

    def applyOperations(self, a1):
        """
        """
        for v1 in range(len(a1) - 1):
            if a1[v1] == a1[v1 + 1]:
                a1[v1], a1[v1 + 1] = (2 * a1[v1], 0)
        v1 = 0
        for v2 in a1:
            if not v2:
                continue
            a1[v1] = v2
            v1 += 1
        for v1 in range(v1, len(a1)):
            a1[v1] = 0
        return a1
