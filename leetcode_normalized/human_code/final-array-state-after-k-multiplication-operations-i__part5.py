class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        if a3 == 1:
            return a1
        for v1 in range(a2):
            v2 = min(range(len(a1)), key=lambda i: a1[v2])
            a1[v2] *= a3
        return a1
