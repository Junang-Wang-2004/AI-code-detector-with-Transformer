class C1(object):

    def closestDivisors(self, a1):
        """
        """

        def divisors(a1):
            for v1 in reversed(range(1, int(a1 ** 0.5) + 1)):
                if a1 % v1 == 0:
                    return (v1, a1 // v1)
            return (1, a1)
        return min([divisors(a1 + 1), divisors(a1 + 2)], key=lambda x: x[1] - x[0])
