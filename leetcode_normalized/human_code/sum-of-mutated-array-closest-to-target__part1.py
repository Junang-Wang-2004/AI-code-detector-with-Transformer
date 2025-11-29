class C1(object):

    def findBestValue(self, a1, a2):
        """
        """
        a1.sort(reverse=True)
        v1 = a1[0]
        while a1 and a1[-1] * len(a1) <= a2:
            a2 -= a1.pop()
        return v1 if not a1 else (2 * a2 + len(a1) - 1) // (2 * len(a1))
