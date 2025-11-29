class C1(object):

    def numberGame(self, a1):
        """
        """
        a1.sort()
        for v1 in range(0, len(a1), 2):
            a1[v1], a1[v1 + 1] = (a1[v1 + 1], a1[v1])
        return a1
