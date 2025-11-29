class C1(object):

    def nextPermutation(self, a1):
        """
        """
        v1, v2 = (-1, 0)
        for v3 in range(len(a1) - 1):
            if a1[v3] < a1[v3 + 1]:
                v1 = v3
        if v1 == -1:
            a1.reverse()
            return
        for v3 in range(v1 + 1, len(a1)):
            if a1[v3] > a1[v1]:
                v2 = v3
        a1[v1], a1[v2] = (a1[v2], a1[v1])
        a1[v1 + 1:] = a1[:v1:-1]
