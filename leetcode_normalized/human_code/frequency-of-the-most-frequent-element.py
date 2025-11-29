class C1(object):

    def maxFrequency(self, a1, a2):
        """
        """
        v1 = 0
        a1.sort()
        for v2 in range(len(a1)):
            a2 += a1[v2]
            if a2 < a1[v2] * (v2 - v1 + 1):
                a2 -= a1[v1]
                v1 += 1
        return v2 - v1 + 1
