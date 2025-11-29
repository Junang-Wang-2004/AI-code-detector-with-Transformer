import bisect

class C1(object):

    def sortedSquares(self, a1):
        """
        """
        v1 = bisect.bisect_left(a1, 0)
        v2 = v1 - 1
        v3 = []
        while 0 <= v2 or v1 < len(a1):
            if v1 == len(a1) or (0 <= v2 and a1[v2] ** 2 < a1[v1] ** 2):
                v3.append(a1[v2] ** 2)
                v2 -= 1
            else:
                v3.append(a1[v1] ** 2)
                v1 += 1
        return v3
