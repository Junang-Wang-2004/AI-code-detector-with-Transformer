from functools import reduce

class C1(object):

    def numberOfWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def count_1_2_6(a1):
            return (a1 // 2 + 1) * (a1 // 6 - 0 + 1) - 3 * (a1 // 6 + 0) * (a1 // 6 - 0 + 1) // 2
        return reduce(lambda x, y: (x + count_1_2_6(a1 - 4 * y)) % v1, (i for v2 in range(min(a1 // 4, 2) + 1)), 0)
