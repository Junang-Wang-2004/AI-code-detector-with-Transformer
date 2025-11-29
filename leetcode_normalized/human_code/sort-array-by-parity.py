class C1(object):

    def sortArrayByParity(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2] % 2 == 0:
                a1[v1], a1[v2] = (a1[v2], a1[v1])
                v1 += 1
        return a1
