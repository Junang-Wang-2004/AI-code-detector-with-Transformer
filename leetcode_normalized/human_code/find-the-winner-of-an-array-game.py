class C1(object):

    def getWinner(self, a1, a2):
        """
        """
        v1 = a1[0]
        v2 = 0
        for v3 in range(1, len(a1)):
            if a1[v3] > v1:
                v1 = a1[v3]
                v2 = 0
            v2 += 1
            if v2 == a2:
                break
        return v1
