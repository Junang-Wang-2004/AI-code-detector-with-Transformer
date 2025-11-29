class C1(object):

    def findMinArrowShots(self, a1):
        """
        """
        if not a1:
            return 0
        a1.sort()
        v1 = 0
        v2 = 0
        while v2 < len(a1):
            v3 = v2 + 1
            v4 = a1[v2][1]
            while v3 < len(a1) and a1[v3][0] <= v4:
                v4 = min(v4, a1[v3][1])
                v3 += 1
            v1 += 1
            v2 = v3
        return v1
