class C1(object):

    def minDeletionSize(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1[0])):
            for v3 in range(1, len(a1)):
                if a1[v3 - 1][v2] > a1[v3][v2]:
                    v1 += 1
                    break
        return v1
