class C1(object):

    def validSquare(self, a1, a2, a3, a4):
        """
        """

        def dist(a1, a2):
            return (a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2
        v1 = set([dist(a1, a2), dist(a1, a3), dist(a1, a4), dist(a2, a3), dist(a2, a4), dist(a3, a4)])
        return 0 not in v1 and len(v1) == 2
