class C1(object):

    def findLongestChain(self, a1):
        """
        """
        a1.sort(key=lambda x: x[1])
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            if v3 == 0 or a1[v2][1] < a1[v3][0]:
                v1 += 1
                v2 = v3
        return v1
