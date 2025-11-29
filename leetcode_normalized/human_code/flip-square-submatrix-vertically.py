class C1(object):

    def reverseSubmatrix(self, a1, a2, a3, a4):
        """
        """
        for v1 in range(a4 // 2):
            for v2 in range(a4):
                a1[a2 + v1][a3 + v2], a1[a2 + (a4 - 1 - v1)][a3 + v2] = (a1[a2 + (a4 - 1 - v1)][a3 + v2], a1[a2 + v1][a3 + v2])
        return a1
