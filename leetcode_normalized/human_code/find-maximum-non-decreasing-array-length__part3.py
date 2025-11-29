import bisect

class C1(object):

    def findMaximumLength(self, a1):
        """
        """
        v1 = v2 = v3 = 0
        v4 = [(0, 0, 0)]
        for v5 in range(len(a1)):
            v2 += a1[v5]
            v3 = bisect.bisect_left(v4, (v2 + 1, 0, 0)) - 1
            v6, v1 = (v2 - v4[v3][1], v4[v3][2] + 1)
            while v4 and v4[-1][0] >= v6 + v2:
                v4.pop()
            v4.append((v6 + v2, v2, v1))
        return v1
