class C1(object):

    def minSwaps(self, a1):
        """
        """
        v1 = v2 = v3 = a1.count(1)
        for v4 in range(len(a1) + (v3 - 1)):
            if v4 >= v3:
                v2 += a1[(v4 - v3) % len(a1)]
            v2 -= a1[v4 % len(a1)]
            v1 = min(v1, v2)
        return v1
