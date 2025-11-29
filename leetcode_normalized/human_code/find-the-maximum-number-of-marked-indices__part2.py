class C1(object):

    def maxNumOfMarkedIndices(self, a1):
        """
        """
        a1.sort()
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2] >= 2 * a1[v1]:
                v1 += 1
        return min(v1, len(a1) // 2) * 2
