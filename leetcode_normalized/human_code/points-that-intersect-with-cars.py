class C1(object):

    def numberOfPoints(self, a1):
        """
        """
        a1.sort()
        v1 = 0
        v2 = a1[0]
        for v3 in range(1, len(a1)):
            if a1[v3][0] <= v2[1]:
                v2[1] = max(v2[1], a1[v3][1])
            else:
                v1 += v2[1] - v2[0] + 1
                v2 = a1[v3]
        v1 += v2[1] - v2[0] + 1
        return v1
