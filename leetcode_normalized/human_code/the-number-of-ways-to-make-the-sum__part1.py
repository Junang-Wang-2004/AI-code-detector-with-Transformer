from functools import reduce

class C1(object):

    def numberOfWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        return (1 + (a1 // 2 + 1) * (a1 // 2) // 2) % v1
