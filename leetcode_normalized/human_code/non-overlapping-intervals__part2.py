class C1(object):

    def eraseOverlapIntervals(self, a1):
        """
        """
        a1.sort(key=lambda interval: interval[0])
        v1, v2 = (0, 0)
        for v3 in range(1, len(a1)):
            if a1[v3][0] < a1[v2][1]:
                if a1[v3][1] < a1[v2][1]:
                    v2 = v3
                v1 += 1
            else:
                v2 = v3
        return v1
