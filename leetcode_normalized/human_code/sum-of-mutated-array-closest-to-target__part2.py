class C1(object):

    def findBestValue(self, a1, a2):
        """
        """
        a1.sort(reverse=True)
        v1 = a1[0]
        while a1 and a1[-1] * len(a1) <= a2:
            a2 -= a1.pop()
        if not a1:
            return v1
        v3 = (a2 - 1) // len(a1)
        return v3 if a2 - v3 * len(a1) <= (v3 + 1) * len(a1) - a2 else v3 + 1
