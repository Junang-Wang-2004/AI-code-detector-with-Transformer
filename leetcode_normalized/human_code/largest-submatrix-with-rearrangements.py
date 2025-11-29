class C1(object):

    def largestSubmatrix(self, a1):
        """
        """
        for v1 in range(len(a1[0])):
            v2 = 0
            for v3 in range(len(a1)):
                v2 = v2 + 1 if a1[v3][v1] == 1 else 0
                a1[v3][v1] = v2
        v4 = 0
        for v5 in a1:
            v5.sort()
            for v1 in range(len(v5)):
                v4 = max(v4, (len(v5) - v1) * v5[v1])
        return v4
