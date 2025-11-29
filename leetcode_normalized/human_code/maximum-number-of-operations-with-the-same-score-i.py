class C1(object):

    def maxOperations(self, a1):
        """
        """
        v1 = 1
        v2 = a1[0] + a1[1]
        for v3 in range(2, len(a1) - 1, 2):
            if a1[v3] + a1[v3 + 1] != v2:
                break
            v1 += 1
        return v1
