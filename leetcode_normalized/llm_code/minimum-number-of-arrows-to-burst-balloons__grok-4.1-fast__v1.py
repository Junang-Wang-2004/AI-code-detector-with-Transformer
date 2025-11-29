class C1(object):

    def findMinArrowShots(self, a1):
        if not a1:
            return 0
        a1.sort(key=lambda x: x[1])
        v1 = 0
        v2 = float('-inf')
        for v3, v4 in a1:
            if v3 > v2:
                v1 += 1
                v2 = v4
        return v1
