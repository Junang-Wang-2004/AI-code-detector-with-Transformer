class C1(object):

    def closestDivisors(self, a1):
        """
        """
        v1, v2 = ([1, a1 + 1], 1)
        while v2 * v2 <= a1 + 2:
            if (a1 + 2) % v2 == 0:
                v1 = [v2, (a1 + 2) // v2]
            if (a1 + 1) % v2 == 0:
                v1 = [v2, (a1 + 1) // v2]
            v2 += 1
        return v1
