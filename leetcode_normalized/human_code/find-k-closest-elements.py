import bisect

class C1(object):

    def findClosestElements(self, a1, a2, a3):
        """
        """
        v1 = bisect.bisect_left(a1, a3)
        v2, v3 = (v1 - 1, v1)
        while a2:
            if v3 >= len(a1) or (v2 >= 0 and abs(a1[v2] - a3) <= abs(a1[v3] - a3)):
                v2 -= 1
            else:
                v3 += 1
            a2 -= 1
        return a1[v2 + 1:v3]
