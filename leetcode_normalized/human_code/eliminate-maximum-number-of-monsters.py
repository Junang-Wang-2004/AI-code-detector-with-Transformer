class C1(object):

    def eliminateMaximum(self, a1, a2):
        """
        """
        for v1 in range(len(a1)):
            a1[v1] = (a1[v1] - 1) // a2[v1]
        a1.sort()
        v2 = 0
        for v1 in range(len(a1)):
            if v2 > a1[v1]:
                break
            v2 += 1
        return v2
