class C1(object):

    def minProcessingTime(self, a1, a2):
        """
        """
        v1 = 4
        a1.sort()
        a2.sort(reverse=True)
        v2 = 0
        for v3 in range(len(a1)):
            for v4 in range(v1):
                v2 = max(v2, a1[v3] + a2[v3 * v1 + v4])
        return v2
