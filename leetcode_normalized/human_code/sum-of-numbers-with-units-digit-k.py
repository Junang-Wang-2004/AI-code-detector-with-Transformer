class C1(object):

    def minimumNumbers(self, a1, a2):
        """
        """
        return next((i for v1 in range(1, (min(a1 // a2, 10) if a2 else 1) + 1) if (a1 - v1 * a2) % 10 == 0), -1) if a1 else 0
