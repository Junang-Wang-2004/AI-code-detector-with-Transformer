class C1(object):

    def maxNumberOfApples(self, a1):
        """
        """
        v1 = 5000
        a1.sort()
        v2, v3 = (0, 0)
        for v4 in a1:
            if v3 + v4 > v1:
                break
            v3 += v4
            v2 += 1
        return v2
