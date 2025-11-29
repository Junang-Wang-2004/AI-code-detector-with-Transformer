class C1(object):

    def moveZeroes(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2]:
                a1[v1] = a1[v2]
                v1 += 1
        for v2 in range(v1, len(a1)):
            a1[v2] = 0
