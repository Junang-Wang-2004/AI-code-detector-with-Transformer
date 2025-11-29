class C1(object):

    def triangleNumber(self, a1):
        """
        """
        v1 = 0
        a1.sort()
        for v2 in reversed(range(2, len(a1))):
            v3, v4 = (0, v2 - 1)
            while v3 < v4:
                if a1[v3] + a1[v4] > a1[v2]:
                    v1 += v4 - v3
                    v4 -= 1
                else:
                    v3 += 1
        return v1
