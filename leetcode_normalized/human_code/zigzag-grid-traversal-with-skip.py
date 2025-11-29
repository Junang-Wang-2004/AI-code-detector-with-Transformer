class C1(object):

    def zigzagTraversal(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1)):
            if v2 % 2 == 0:
                v1.extend((a1[v2][j] for v3 in range(0, len(a1[0]), 2)))
            else:
                v1.extend((a1[v2][v3] for v3 in reversed(range(1, len(a1[0]), 2))))
        return v1
