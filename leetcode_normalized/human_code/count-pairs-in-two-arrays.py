class C1(object):

    def countPairs(self, a1, a2):
        """
        """
        for v1 in range(len(a1)):
            a1[v1] -= a2[v1]
        a1.sort()
        v2 = 0
        v3, v4 = (0, len(a1) - 1)
        while v3 < v4:
            if a1[v3] > 0 or -a1[v3] < a1[v4]:
                v2 += v4 - v3
                v4 -= 1
            else:
                v3 += 1
        return v2
